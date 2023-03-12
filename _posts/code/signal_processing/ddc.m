function [] = demod_realtype(sig_filename, output_filename, SamplingRate, SpreadingFactor, OverSR, NumberPreamble, NumberSync, NumberSFD, Threshold)

fid1 = fopen(sig_filename);
LoRasignal = int16(fread(fid1, Inf, 'int16','ieee-be'));
fclose(fid1);
T = numerictype(1,16,15);
datapart_T = reinterpretcast(LoRasignal, T);
len = length(datapart_T);

datapart_pre = zeros(len,1);
datapart_pre([1:len]) = datapart_T([1:len]);

datapart = datapart_pre(1:2*floor(len/2));

hDDC22 = dsp.DigitalDownConverter(...
    'DecimationFactor', 2, ...
    'SampleRate', SamplingRate, ...
    'Bandwidth', Bandwidth, ...
    'StopbandAttenuation', 10, ...
    'PassbandRipple', 0.6, ...
    'CenterFrequency', Centerfreq);

cplx_datapart = hDDC22.step(datapart);
cplx_datapart = resample(cplx_datapart, 2*Bandwidth,SamplingRate/2);
len_cplx = lenth(cplx_datapart);
