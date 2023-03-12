
`timescale 1ns / 1ps

module Cashier (
    input  wire                     i_clk,
    input  wire                     i_rst,
    input  wire                     i_enable,
    input  wire [15:0]              i_payment,
    input  wire [11:0]              i_item1_price,
    input  wire [2:0]               i_item1_num,
    input  wire [11:0]              i_item2_price,
    input  wire [2:0]               i_item2_num,

    output reg                      o_busy,
    output reg                      o_valid,
    output reg                      o_paid,
    output reg  [15:0]              o_change
);


reg [3:0]        cnt;
reg [15:0]       s_payment;
reg [11:0]       s_item1_price;
reg [2:0]        s_item1_num;
reg [11:0]       s_item2_price;
reg [2:0]        s_item2_num;

wire s_enable = i_enable && (!o_busy);
always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) 
        cnt <= 0;
    else begin
        if (s_enable) 
            cnt <= 1;
        else if (cnt == 4'b1001) 
            cnt <= cnt;
        else
	    cnt <= cnt + 1;
    end
end

// clk cycle counter
// i_enable == 1 -> 1~9 count
// use mult input & control output
// cycle #7 -> multiplier out print
// cycle #8 -> cashier output print
// cycle #9 -> wait for next input

always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) begin
        s_payment <= 0;
        s_item1_price <= 0;
        s_item1_num <= 0;
        s_item2_price <= 0;
        s_item2_num <= 0;
    end
    else begin
        if (s_enable) begin
            s_payment     <= i_payment;
            s_item1_price <= i_item1_price;
            s_item1_num   <= i_item1_num;
            s_item2_price <= i_item2_price;
            s_item2_num   <= i_item2_num;
        end
    end
end

// cnt == 1~6 -> 1, else, 0

reg  mult_en;
always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) 
        mult_en <= 1'b0;
    else begin
        if (s_enable) 
            mult_en <= 1'b1;
        else if (cnt > 4'b0110)
            mult_en <= 1'b0;
    end
end

wire [11:0] price = (cnt < 4'b0100) ? s_item1_price : s_item2_price;
wire [2:0]  num   = (cnt < 4'b0100) ? s_item1_num   : s_item2_num;
wire        mult_valid;
wire [15:0] mult_out;


// import sequential multiplier

seq_mul s_mult (i_clk, i_rst, s_enable, mult_en, price, num, mult_out);


// cnt 1~6 -> multiplier calculation, cnt 7 -> prepare output
always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) 
        o_busy <= 1'b0;
    else begin
        if (i_enable) 
            o_busy <= 1'b1;
        else if (cnt == 4'b0111)
            o_busy <= 1'b0;
    end
end

// prepare valid output @ cnt #7 & print @ cnt #8
always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) 
        o_valid <= 1'b0;
    else begin
        if (cnt == 4'b0111)
            o_valid <= 1'b1;
        else
            o_valid <= 1'b0;
    end
end

wire [15:0] s_change = s_payment - mult_out;
always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst)  begin
        o_paid <= 0;
        o_change <= 0;
    end
    else begin
        if (cnt == 4'b0111) begin // positive
            if (s_change[15] == 1'b0) begin  
                o_change <= s_change;
                o_paid <= 1;
            end
            else begin     //negative                  
                o_change <= 0;
                o_paid <= 0;
            end
        end
        else begin        
            o_change <= 0;
            o_paid <= 0;
        end
    end
end

endmodule
