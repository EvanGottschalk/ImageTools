import os
import sys

from PIL import Image
from moviepy.editor import *

class ImageTools:
    def __init__(self):
        self.input_folder = os.getcwd() + '/inputs/'
        self.output_folder = os.getcwd() + '/outputs/'
        self.resize_output_folder = os.getcwd() + '/resize_outputs/'
        self.crop_output_folder = os.getcwd() + '/crop_outputs/'
        self.combine_output_folder = os.getcwd() + '/combine_outputs/'
        self.landscape_output_folder = os.getcwd() + '/sorted_landscape/'
        self.portrait_output_folder = os.getcwd() + '/sorted_portrait/'
        self.square_output_folder = os.getcwd() + '/sorted_square/'
        self.folder_dict = {'inputs': self.input_folder, \
                            'outputs': self.output_folder, \
                            'resize_outputs': self.resize_output_folder, \
                            'crop_outputs': self.crop_output_folder, \
                            'combine_outputs': self.combine_output_folder, \
                            'landscape_outputs': self.landscape_output_folder, \
                            'portrait_outputs': self.portrait_output_folder, \
                            'square_outputs': self.square_output_folder}

    def sortBatch(self, input_folder=None):
        file_count = 0
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        for file_name in os.listdir(input_folder):
            file_count += 1
            image = Image.open(input_folder + file_name)
            # checks for portrait or landscape by checking if width is greater than height
            if image.size[0] > image.size[1]:
                image.save(self.landscape_output_folder + file_name, quality=100, optimize=True)
            elif image.size[0] < image.size[1]:
                image.save(self.portrait_output_folder + file_name, quality=100, optimize=True)
            else:
                image.sage(self.square_output_folder + file_name, quality=100, optimize=True)
        
    def resizeBatch(self, input_folder=None, output_folder=None, new_width=None, new_height=None, quality=100, number_outputs=False, include_original_name=True):
        file_count = 0
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        if output_folder:
            output_folder = self.folder_dict[output_folder]
        else:
            output_folder = self.resize_output_folder
        for file_name in os.listdir(input_folder):
            file_count += 1
            output_file_name = ''
            if number_outputs:
                output_file_name = str(file_count)
                if include_original_name:
                    output_file_name += '_' + file_name
                else:
                    output_file_name += '.jpg'
            if include_original_name:
                output_file_name += file_name
            image = self.resize(input_file_name=file_name, input_folder=input_folder, output_folder=output_folder, new_width=new_width, new_height=new_height, quality=quality, output_file_name=output_file_name)

    def resize(self, image=None, input_file_name=None, input_folder=None, output_folder=None, new_width=None, new_height=None, quality=100, output_file_name=None):
        if not(input_folder):
            input_folder = self.input_folder
        if not(output_folder):
            output_folder = self.resize_output_folder
        if not(output_file_name):
            output_file_name = input_file_name
        if not(image):
            image = Image.open(input_folder + input_file_name)
            image = image.convert('RGB')
        if not(new_width):
            new_width = int((new_height * image.size[0]) / image.size[1])
        width_percent = (new_width / float(image.size[0]))
        if not(new_height):
            new_height = int(image.size[1] * width_percent)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image.save(output_folder + output_file_name, quality=quality, optimize=True)
        return(image)

    def cropBatch(self, input_folder=None, crop_width=None, crop_height=None, number_outputs=False, include_original_name=True):
        file_count = 0
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        for file_name in os.listdir(input_folder):
            file_count += 1
            output_file_name = ''
            if number_outputs:
                output_file_name = str(file_count)
                if include_original_name:
                    output_file_name += '_' + file_name
            if include_original_name:
                output_file_name += file_name
            image = self.crop(input_file_name=file_name, input_folder=input_folder, crop_width=crop_width, crop_height=crop_height, output_file_name=output_file_name)

    def crop(self, image=None, input_file_name=None, input_folder=None, crop_width=None, crop_height=None, output_file_name=None):
        if not(input_folder):
            input_folder = self.input_folder
        if not(output_file_name):
            output_file_name = input_file_name
        if not(image):
            image = Image.open(input_folder + input_file_name)
        if crop_width:
            image = image.crop(((image.size[0] / 2) - (crop_width / 2), 0, (image.size[0] / 2) + (crop_width / 2), image.size[1]))
        if crop_height:
            image = image.crop((0, (image.size[1] / 2) - (crop_height / 2), image.size[0], (image.size[1] / 2) + (crop_height / 2)))
        image.save(self.crop_output_folder + output_file_name)
        return(image)
        
    def combineBatch(self, base_image_name, input_folder=None, added_image_position='top', output_height=None, output_width=None, \
                     number_outputs=False, include_original_name=True):
        file_count = 0
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        for file_name in os.listdir(input_folder):
            file_count += 1
            output_file_name = ''
            if number_outputs:
                output_file_name = str(file_count)
                if include_original_name:
                    output_file_name += '_' + file_name
                else:
                    output_file_name += '.png'
            if include_original_name:
                output_file_name += file_name
            combined_image = self.combine(base_image_name, file_name, input_folder=input_folder, output_file_name=output_file_name, added_image_position=added_image_position)

    def combine(self, base_image_name, added_image_name, input_folder=None, output_folder=None, added_image_position='top', output_file_name='output', output_height=None, output_width=None):
        if not(input_folder):
            input_folder = self.input_folder
        if not(output_folder):
            output_folder = self.combine_output_folder
        base_image = Image.open(base_image_name).convert("RGBA")
        added_image = Image.open(input_folder + added_image_name).convert("RGBA")
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
        combined_image.save(output_folder + output_file_name, 'PNG')
        return(base_image)

    def randomizeResize(self, image, intensity=5):
        max_image_width = min(image.width * 1.05, self.image_width)
        min_image_width = image.width * (1 - ((2 * intensity)/100) - (max_image_width / image.width))

    def generateRectangle(self, width=1000, height=1000, x=0, y=0, stroke=30, color=(255, 255, 255)):
##        for num_x in range(x, x + width):
##            for num_y in range(y, y + stroke):
##                self.new_image.putpixel((num_x, num_y), color)
        new_image = ImageDraw.Draw(self.new_image)
        new_image.line([(x, y), (x + width, y)], fill=color, width=stroke)
        new_image.line([(x, y), (x, y + height)], fill=color, width=stroke)
        new_image.line([(x, y + height), (x + width, y + height)], fill=color, width=stroke)
        new_image.line([(x + width, y), (x + width, y + height)], fill=color, width=stroke)


    def compress(self):
        shit = 'balls'

    def compressBatch(self):
        shit = 'balls'

    def combineVideo(self, base_image_name, video_name, input_folder=None, output_folder=None, duration=4, added_image_position='top', output_file_name='output', output_height=None, output_width=None):
        video_file = VideoFileClip(video_name)
        image_clip = (ImageClip(base_image_name)
           .set_start(0) #which second to start displaying image
           .set_duration(duration) #how long to display image
           .set_position(("center", "bottom")))
        combined_video = CompositeVideoClip([video_file, image_clip])
        combined_video.write_videofile(output_file_name + '.mp4')

IT = ImageTools()

### Sort
#IT.sortBatch(input_folder='inputs')


### Portrait
##IT.resizeBatch(input_folder='portrait_outputs', new_width=930)
##IT.cropBatch(input_folder='resize_outputs', crop_height=1017)
##IT.combineBatch(input_folder='crop_outputs', base_image_name='portrait_bumper.png', number_outputs=True, include_original_name=False)
####IT.resizeBatch(input_folder='combine_outputs', output_folder='outputs', new_height=693, quality=85, number_outputs=True, include_original_name=False)
##

### Landscape
IT.resizeBatch(input_folder='landscape_outputs', new_width=1280)
IT.cropBatch(input_folder='resize_outputs', crop_height=592)
IT.combineBatch(input_folder='crop_outputs', base_image_name='landscape_bumper.png', number_outputs=True, include_original_name=False)
####IT.resizeBatch(input_folder='combine_outputs', output_folder='outputs', new_height=693, quality=85, number_outputs=True, include_original_name=False)


### Videos
#IT.combineVideo(base_image_name='input_bumper.png', video_name='test_video.mp4', input_folder='inputs', output_folder='outputs')
