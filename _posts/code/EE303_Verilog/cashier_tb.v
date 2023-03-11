`timescale 1 ns/ 1 ps

module cashier_tb;

reg                      i_clk;
reg                      i_rst;
reg                      i_enable;
reg  [15:0]              i_payment;
reg  [11:0]              i_item1_price;
reg  [2:0]               i_item1_num;
reg  [11:0]              i_item2_price;
reg  [2:0]               i_item2_num;

wire                      o_busy;
wire                      o_valid;
wire                      o_paid;
wire  [15:0]              o_change;

initial i_clk = 1;
always #5 i_clk = ~i_clk;

initial begin
    i_rst = 1;
#21 i_rst = 0; 
    i_enable = 1;
    i_payment = 10000;
    i_item1_price = 3500;
    i_item1_num = 2;
    i_item2_price = 1000;
    i_item2_num = 2;

#10 i_enable = 0;
#100 
    i_enable = 1;
    i_payment = 5000;
    i_item1_price = 2000;
    i_item1_num = 2;
    i_item2_price = 1000;
    i_item2_num = 1;

#10 i_enable = 0;
#100 
    i_enable = 1;
    i_payment = 5000;
    i_item1_price = 2000;
    i_item1_num = 2;
    i_item2_price = 1000;
    i_item2_num = 2;



#10 i_enable = 0;
#100 
    i_enable = 1;
    i_payment = 65535;
    i_item1_price = 4095;
    i_item1_num = 7;
    i_item2_price = 4095;
    i_item2_num = 7;
#10 i_enable = 0;

end

Cashier u0 (i_clk, i_rst, i_enable, i_payment, i_item1_price, i_item1_num,
	    i_item2_price, i_item2_num, o_busy, o_valid, o_paid, o_change);

endmodule
                                
