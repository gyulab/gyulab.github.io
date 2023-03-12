`timescale 1ns / 1ps

module seq_mul (
    input  wire                     i_clk,
    input  wire                     i_rst,
    input  wire                     i_enable,
    input  wire                     i_sm_en,
    input  wire [11:0]              i_price,
    input  wire [2:0]               i_num,
    output reg  [15:0]              o_result
);

integer snum;

//counter determines shift or not
// 0,1,2 count to do multiplication twice

always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) 
        snum <= 0;
    else begin
        if (i_sm_en) begin
            if (snum == 2)
                snum <= 0;
            else
                snum <= snum + 1;
        end
        else
            snum <= 0;
    end
end 

//identify 1 or 0, if 1, shift and sum
always @ (posedge i_clk, posedge i_rst)
begin
    if (i_rst) 
        o_result <= 0;
    else begin
        //clear sum i_enable asserted, if not, accumulate sum
        if (i_enable)
            o_result <= 0;
        else if (i_sm_en) begin
            //position of 1- i_price shift w.r.t. i_num
            if (i_num[snum] == 1'b1) 
                o_result <= o_result + (i_price << snum); 
        end
    end
end


endmodule
