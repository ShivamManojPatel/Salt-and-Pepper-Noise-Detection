#Project 4: Algorithm design and implementation
#Course: CSCI 4353 / 5353 Multimedia Computing
#Team Members: Shivam Patel, Mason Simpson
#Date: November 18, 2025
#Description: This project implements a multimedia computing algorithm that processes images and videos to enhance their quality using advanced filtering techniques.
#--------------------------------------------------------------

import cv2
import numpy as np
import math

#Defining utility functions
def calculate_mse(img1, img2): #formula: MSE = (1/N) * Σ (I1 - I2)^2
    #---Calculating Mean Squared Error (MSE) between two images---#
    diff = np.subtract(np.float64(img1), np.float64(img2))
    mse = np.mean(np.square(diff))
    return mse

def calculate_snr(img1, img2): #formula: SNR = 10 * log10(Psignal / Pnoise), Psignal = mean(I1^2), Pnoise = mean((I1 - I2)^2)
    #---Calculating Signal-to-Noise Ratio (SNR) between two images---#
    signal_power = np.mean(np.square(np.float64(img1)))
    noise_power = np.mean(np.square(np.float64(img1) - np.float64(img2)))
    if noise_power == 0:
        return float('inf')
    snr = 10 * math.log10(signal_power / noise_power)
    return snr

def calculate_psnr(img1, img2): #formula: PSNR = 10 * log10((MAX_I^2) / MSE), MAX_I = 255 for 8-bit images
    #---Calculating Peak Signal-to-Noise Ratio (PSNR) between two images---#
    mse = calculate_mse(img1, img2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 10 * math.log10((max_pixel ** 2) / mse)
    return psnr

def print_metrics(title, mse, snr, psnr): #simple function to print metrics
    print(f"===== {title} =====")
    print(f"MSE: {mse:4f}")
    print(f"SNR: {snr:4f} dB")
    print(f"PSNR: {psnr:4f} dB")
    print()

#--- Step 1: Load the images ---#
original = cv2.imread(r"<Relative path for your original image>", cv2.IMREAD_GRAYSCALE)
noisy = cv2.imread(r"{<Relative path for your noisy image>", 0)

if original is None or noisy is None:
    raise FileNotFoundError("One or both image files not found.") #exception in case files are not found

print("Step 1..............................Complete")

#--- Step 2: Calculate MSE, SNR, psnr for noisy image ---#
MSE1 = calculate_mse(original, noisy)
SNR1 = calculate_snr(original, noisy)
PSNR1 = calculate_psnr(original, noisy)

print("Step 2..............................Complete")

#--- Step 3: Apply 3X3 average filter ---#
avg_filtered = cv2.blur(noisy, (3, 3)) #3x3 average filter
cv2.imwrite(r'<Relative path of your folder where you want to save image>\Averaged.jpg', avg_filtered) #save the image as Lena_averaged.jpg

MSE2 = calculate_mse(original, avg_filtered)
SNR2 = calculate_snr(original, avg_filtered)
PSNR2 = calculate_psnr(original, avg_filtered)

print("Step 3..............................Complete")

#--- Step 4: Apply 3X3 median filter ---#
median_filtered = cv2.medianBlur(noisy, 3) #3x3 median filter
cv2.imwrite(r'<Relative path of your folder where you want to save image>\Median.jpg', median_filtered) #save the image as Lena_median.jpg

MSE3 = calculate_mse(original, median_filtered)
SNR3 = calculate_snr(original, median_filtered)
PSNR3 = calculate_psnr(original, median_filtered)

print("Step 4..............................Complete")

#--- Step 5: Noise detection algorithm ---#
def detect_noise(img): #function to detect noisy pixels
    #--- Detect noisy pixel (Salt & Pepper noise) ---#
    h, w = img.shape
    detected = np.zeros((h, w, 3), dtype=np.uint8)
    detected[:, :] = (128, 128, 128)

    detected[img == 0] = (0,0,0)
    detected[img == 255] = (255,255,255)

    noise_mask = (img == 0) | (img == 255)
    
    return noise_mask.astype(np.uint8), detected

noise_mask, detected_noise_image = detect_noise(noisy)
cv2.imwrite(r'<Relative path of your folder where you want to save image>\Noise_detected.jpg', detected_noise_image) #save the image as Lena_noise_detected.jpg

print("Step 5..............................Complete")

#--- Step 6: Apply Median filter only on detected noisy pixels ---#
median_filtered_full = cv2.medianBlur(noisy, 3) 
selective_filtered = noisy.copy() 

#replace only noisy pixels
selective_filtered[noise_mask == 1] = median_filtered_full[noise_mask == 1] #apply median filter only on detected noisy pixels
cv2.imwrite(r'<Relative path of your folder where you want to save image>\Median_selective.jpg', selective_filtered) #save the image as Lena_median_selective.jpg

MSE4 = calculate_mse(original, selective_filtered)
SNR4 = calculate_snr(original, selective_filtered)
PSNR4 = calculate_psnr(original, selective_filtered)

print("Step 6..............................Complete")

#--- Step 7: Assess Effectivenss ---#
diff_MSE = abs(MSE1 - MSE4)
diff_SNR = abs(SNR1 - SNR4)
diff_PSNR = abs(PSNR1 - PSNR4)

diff_MSE_percent = (diff_MSE / MSE1) * 100 if MSE1 != 0 else 0 #to avoid division by zero
diff_SNR_percent = (diff_SNR / SNR1) * 100 if SNR1 != 0 else 0
diff_PSNR_percent = (diff_PSNR / PSNR1) * 100 if PSNR1 != 0 else 0

print("Step 7..............................Complete")

#--- Final Output ---#

print("----------------Final Output----------------")

print_metrics("Lena_noisy.jpg", MSE1, SNR1, PSNR1)
print_metrics("Lena_averaged.jpg", MSE2, SNR2, PSNR2)
print_metrics("Lena_median.jpg", MSE3, SNR3, PSNR3)
print_metrics("Lena_median_selective.jpg", MSE4, SNR4, PSNR4)

print("===== Effectiveness Assessment =====")
print(f"Difference in MSE: {diff_MSE:4f} ({diff_MSE_percent:4f}%)")
print(f"Difference in SNR: {diff_SNR:4f} dB ({diff_SNR_percent:4f}%)")
print(f"Difference in PSNR: {diff_PSNR:4f} dB ({diff_PSNR_percent:4f}%)")

print("-------------Project 4 Complete-------------")

#--- End of Project 4 ---#
