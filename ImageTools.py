import os
import sys

from PIL import Image

class ImageTools:
    def __init__(self):
        self.input_folder = os.getcwd() + '/inputs/'
        self.output_folder = os.getcwd() + '/outputs/'

    def resizeBatch(new_width=None, new_height=None, number_outputs=False, include_original_name=True):
        file_count = 0
        for file_name in os.listdir(self.starting_folder):
            file_count += 1
            output_file_name = ''
            if number_outputs:
                output_file_name = str(file_count)
                if include_original_name:
                    output_file_name += '_' + file_name
            if include_original_name:
                output_file_name += file_name
            self.resize(file_name, new_width, new_height, output_file_name)

    def resize(self, input_file_name, new_width=None, new_height=None, output_file_name=None):
        if not(output_file_name):
            output_file_name = input_file_name
        image = Image.open(self.input_folder + input_file_name)
        if not(new_width):
            new_width = (new_height * image.size[0]) / image.size[1]   
        width_percent = (new_width / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image.save(self.output_folder + output_file_name)
        return(image)

    def combine(self, base_image_name, added_image_name, added_image_position='top', output_file_name='output', output_height=None, output_width=None):
        base_image = Image.open(base_image_name).convert("RGBA")
        added_image = Image.open(self.input_folder + added_image_name).convert("RGBA")
        # output dimensions are calculated
        if not(output_height):
            if added_image_position == 'bottom' or added_image_position == 'top':
                output_height = base_image.size[1] + added_image.size[1]
            else:
                output_height = max(base_image.size[1], added_image.size[1])
        if not(output_width):
            if added_image_position == 'bottom' or added_image_position == 'top':
                output_width = max(base_image.size[0], added_image.size[0])
            else:
                output_width = base_image.size[0] + added_image.size[0]
        # image positions are calculated
        if added_image_position == 'bottom' or added_image_position == 'top':
            base_image_x = 0
            added_image_x = 0
            if added_image_position == 'bottom':
                base_image_y = 0
                added_image_y = base_image.size[1]
            else:
                base_image_y = added_image.size[1]
                added_image_y = 0
        else:
            base_image_y = 0
            added_image_y = 0
            if added_image_position == 'right':
                base_image_x = 0
                added_image_x = base_image.size[0]
            else:
                base_image_x = added_image.size[0]
                added_image_x = 0
        combined_image = Image.new("RGBA", (output_width, output_height))
        combined_image.paste(base_image, (base_image_x, base_image_y), base_image)
        combined_image.paste(added_image, (added_image_x, added_image_y), added_image)
        combined_image.save(self.output_folder + output_file_name, 'PNG')
        return(base_image)

    def combineBatch(self, base_image_name, added_image_position='top', output_height=None, output_width=None, \
                     number_outputs=False, include_original_name=True):
        file_count = 0
        for file_name in os.listdir(self.input_folder):
            file_count += 1
            output_file_name = ''
            if number_outputs:
                output_file_name = str(file_count)
                if include_original_name:
                    output_file_name += '_' + file_name
            if include_original_name:
                output_file_name += file_name
            combined_image = self.combine(base_image_name, file_name, output_file_name=output_file_name, added_image_position=added_image_position)

    def compress(self):
        shit = 'balls'

    def compressBatch(self):
        shit = 'balls'
        
        

IT = ImageTools()
IT.combineBatch('Celebrity Softball Classic 2022 Bumper.png')

