# Salt and Pepper Noise Detection

-------------------------------------
Description
-------------------------------------
This is an academic project that implements image noise evaluation, filtering, and selective noise removal techniques using Python and OpenCV.
The goal is to analyze a noisy version of an image, measure the image degradation using MSE, SNR, and PSNR, and improve the image quality using average filter, median filter, and a custom noise-detection algorithm.

-------------------------------------
Features
-------------------------------------
- Compute MSE, SNR, and PSNR between the original and noisy images
- Apply 3x3 average filter
- Apply 3x3 median filter
- Implement a custom salt-and-pepper noise detection algorithm
- Apply the median filter only to the detected noisy pixels
- Generate all processed output images
- Evaluate improvements using comparison tables

-------------------------------------
Algorithm used
-------------------------------------
Average Filter
  - Smooths the image by replacing each pixel with the mean of its 3x3 neighbors. Helps reduce noise but also introduces blur

Median Filter
  - Replaces each pixel with the median of its 3x3 neighbors. Very effective for removing salt-and-pepper noise while preserving edges.

Noise Detection Algorithm (Custom)
  - Detects noisy pixels by checking if their intensity is either 0 or 255, which are characteristic values of salt-and-pepper noise.
  - noise_mask - (img == 0) | (img == 255)

Selective Median Filter
  - Instead of filtering the entire image, only noisy pixels identified by the mask are replaced with their median-filtered value.
 
-------------------------------------
Output images
-------------------------------------
- Averaged.jpg
- Median.jpg
- Noise_detected.jpg (Gray background showing noise)
- Median_selective.jpg

Note: The names of output images in the project repository are different because we had certain guidelines for our academic project. But we have modified the code to produce images that are listed above. This code is not limited to the Lena image. You can operate on your images too, just follow the  **How to run code** section.

-------------------------------------
Minor feature
-------------------------------------
- Role-based access control (Different login flow for customer and admin. But, same login page).
- Secure integration payment gateway using Stripe.
- Booking status based on stage of booking for better understanding (Pending, confirmed, cancelled, completed).
- Filters for sorting cars for a better surfing experience (by price range, brand, transmission type, etc).
- Logging in before renting or making a reservation for security and audit.

-------------------------------------
Output Metrics
-------------------------------------
Evaluation Metrics
|--------------------------|---------------|---------------|---------------| <br>
|**Image**                 |**MSE**        |**SNR**        |**PSNR**       | <br>
|--------------------------|---------------|---------------|---------------| <br>
|Lena_noise.jpg            |235.088144     |16.881154      |24.418496      | <br>
|                          |               |               |               | <br>
|Lena_average.jpg          |40.043867      |24.568101      |32.10444       | <br>
|                          |               |               |               | <br>
|Lena_median.jpg           |15.734956      |28.624806      |36.162148      | <br>
|                          |               |               |               | <br>
|Lena_median_selective.jpg |122.008578     |36.162148      |27.266900      | <br>
|--------------------------|---------------|---------------|---------------| <br>

Effetiveness Assessment Example
|------------|-----------------|----------------------------|-------------------|-------------------|
|**Metric**  |**Noisy**        |**Selective Median**        |**Difference**     |**Difference(%)**  |
|------------|-----------------|----------------------------|-------------------|-------------------|
|MSE         |235.088144       |122.008578                  |113.079567         |48.100923%         |
|            |                 |                            |                   |                   |
|SNR         |16.881154        |19.729557                   |2.848404           |16.873276%         |
|            |                 |                            |                   |                   |
|PSNR        |24.418496        |27.266900                   |2.848404           |11.664943%         |
|------------|-----------------|----------------------------|-------------------|-------------------|

-------------------------------------
How to run code
-------------------------------------
- Install dependencies
  - pip install opencv-python numpy

- replace image names at lines 45 & 46.
  - Input requires the original image for metric evaluation and the noisy image to perform the algorithm.

-------------------------------------
Author
-------------------------------------
**Shivam Patel, Mason Simpson** <br>
University of Central Arkansas | Department of Computer Science

