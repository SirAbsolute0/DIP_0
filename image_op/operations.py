import numpy as np
import cv2

class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """

        # add your code here
        
        #Merging directly on left image
        for y in range(column, image_right.shape[1]):
            for x in range(0, image_right.shape[0]):
                image_left[x,y] = image_right[x,y]

        # Please do not change the structure
        return image_left  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here
        
        #Create a copy of the orginal input picture
        intensity_image = input_image.copy()

        #Multiply every value of the left side with alpha
        for y in range(0, column):
            for x in range(0, intensity_image.shape[0]):
                intensity_image[x,y] = intensity_image[x,y] * alpha
        
        #Multiply every value of the right side with beta
        for y in range(column, intensity_image.shape[1]):
            for x in range(0, intensity_image.shape[0]):
                intensity_image[x,y] = intensity_image[x,y] * beta

        # Please do not change the structure
        return intensity_image  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """
        # add your code here

        #Create a copy version of the original picture
        central_image = input_image.copy()

        #Variables
        left_intensity = 0
        left_counter = 0

        right_intensity = 0
        right_counter = 0

        left_offset = 0
        right_offset = 0

        #Going through each pixels on the left and sum the total intensity
        for y in range(0, column):
            for x in range(0, central_image.shape[0]):
                left_intensity += central_image[x,y]
                left_counter +=1
        
        #Going through each pixels on the right and sum the total intensity
        for y in range(column, central_image.shape[1]):
            for x in range(0, central_image.shape[0]):
                right_intensity += central_image[x,y]
                right_counter +=1
        
        #Calculating the offset        
        left_offset = 128 - (left_intensity/left_counter)
        right_offset = 128 - (right_intensity/right_counter)
        
        #Adding each pixels on the left side with the offset and capping off values bottom/top
        temp_value = 0.0
        for y in range(0, column):
            for x in range(0, central_image.shape[0]):
                temp_value = central_image[x,y].copy()
                temp_value += left_offset
                
                if (temp_value < 0):
                    central_image[x,y] = 0
                elif(temp_value > 255):
                    central_image[x,y] = 255
                else:
                    central_image[x,y] = temp_value
        
        #Adding each pixels on the right side with the offset and capping off values bottom/top
        for y in range(column, central_image.shape[1]):
            for x in range(0, central_image.shape[0]):
                temp_value = central_image[x,y].copy()
                temp_value += left_offset
                
                if (temp_value < 0):
                    central_image[x,y] = 0
                elif(temp_value > 255):
                    central_image[x,y] = 255
                else:
                    central_image[x,y] = temp_value

        return central_image   # Currently the input image is returned, please replace this with the centralized image