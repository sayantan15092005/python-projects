import cv2
import numpy as np

def remove_background(image_path, output_path):
    try:
        # Read the input image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to read the image at {image_path}. Please check the file path.")
            return
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to smooth the image
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Thresholding to create a binary mask
        _, mask = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Create an empty mask for the largest contour
        largest_contour_mask = np.zeros_like(mask)
        
        if contours:
            # Find the largest contour by area
            largest_contour = max(contours, key=cv2.contourArea)
            # Draw the largest contour on the mask
            cv2.drawContours(largest_contour_mask, [largest_contour], -1, (255), thickness=cv2.FILLED)
        
        # Create a new image with the background removed
        result = cv2.bitwise_and(image, image, mask=largest_contour_mask)
        
        # Save the result
        cv2.imwrite(output_path, result)
        print(f"Background removed successfully. Output saved at {output_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "test2.png"  # Replace with the path to your input image
    output_image_path = "output.jpg"  # Replace with the desired output path
    remove_background(input_image_path, output_image_path)