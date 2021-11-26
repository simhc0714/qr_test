# -*- coding: utf-8 -*-

#%%
import qrcode

#%%
dat_text = 'EA.hy926,20210415,0'
img = qrcode.make(dat_text)

#%% invert comma to hyphen
"""
dat_name = dat_text.replace(",","-")
file_name = dat_name + '.png'
"""

file_name = dat_text.replace(",","-") + '.png'

print(file_name)
#%% qr image save
img.save(file_name)

#%% Advanced Usage
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

dat2_text = 'EA.hy926,20210415,0'
qr.add_data(dat2_text)
qr.make(fit=True)

file2_name = dat2_text.replace(",","-") + '.png'
img = qr.make_image(fill_color="black", back_color="white")
img.save(file2_name)