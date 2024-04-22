import os
import sys
import shutil

from PIL import Image
from moviepy.editor import *

class ImageTools:
    def __init__(self):
        self.input_folder = os.getcwd() + '/inputs/'
        self.output_folder = os.getcwd() + '/outputs/'
        self.resize_output_folder = os.getcwd() + '/resize_outputs/'
        self.crop_output_folder = os.getcwd() + '/crop_outputs/'
        self.append_output_folder = os.getcwd() + '/append_outputs/'
        self.overlay_output_folder = os.getcwd() + '/overlay_outputs/'
        self.landscape_output_folder = os.getcwd() + '/sorted_landscape/'
        self.portrait_output_folder = os.getcwd() + '/sorted_portrait/'
        self.square_output_folder = os.getcwd() + '/sorted_square/'
        self.folder_dict = {'inputs': self.input_folder, \
                            'outputs': self.output_folder, \
                            'resize_outputs': self.resize_output_folder, \
                            'crop_outputs': self.crop_output_folder, \
                            'append_outputs': self.append_output_folder, \
                            'overlay_outputs': self.overlay_output_folder, \
                            'landscape_outputs': self.landscape_output_folder, \
                            'portrait_outputs': self.portrait_output_folder, \
                            'square_outputs': self.square_output_folder}

    def createBlankImage(self, width, height):
        new_blank_image = Image.new("RGBA", (width, height))
        return(new_blank_image)

    def saveImage(self, image, destination, file_name):
        image.save(destination + '/' + file_name, quality=100, optimize=True)

    def sortBatch(self, input_folder=None, clear_output_folder=False):
        file_count = 0
        # Set input folder
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        # Delete output folders
        if clear_output_folder:
            shutil.rmtree(self.landscape_output_folder)
            shutil.rmtree(self.portrait_output_folder)
        # Create new folders if they don't exist
        if not(os.path.isdir(self.landscape_output_folder)):
            os.mkdir(self.landscape_output_folder)
        if not(os.path.isdir(self.portrait_output_folder)):
            os.mkdir(self.portrait_output_folder)
        # Sort through files in input folders
        for file_name in os.listdir(input_folder):
            file_count += 1
            image = Image.open(input_folder + file_name)
            # checks for portrait or landscape by checking if width is greater than height
            if image.size[0] > image.size[1]:
                image.save(self.landscape_output_folder + file_name, quality=100, optimize=True)
            elif image.size[0] < image.size[1]:
                image.save(self.portrait_output_folder + file_name, quality=100, optimize=True)
            else:
                image.save(self.square_output_folder + file_name, quality=100, optimize=True)
        
    def resizeBatch(self, input_folder=None, output_folder=None,
                    new_width=None, new_height=None, quality=100,
                    number_outputs=False, include_original_name=True,
                    clear_output_folder=False):
        file_count = 0
        # Set input folder
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        # Set output folder
        if output_folder:
            output_folder = self.folder_dict[output_folder]
        else:
            output_folder = self.resize_output_folder
        # Delete output folder
        if clear_output_folder:
            try:
                shutil.rmtree(output_folder)
            except Exception:
                error = Exception
        # Create output folder
        if not(os.path.isdir(output_folder)):
            os.mkdir(output_folder)
        # Resize files in input folder
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

    def resize(self, image=None, input_file_name=None, input_folder=None, output_folder=None,
               new_width=None, new_height=None, quality=100, output_file_name=None):
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
        try:
            image = self.premultiply(image)
        except:
            print('Premultiply before resizing FAILED!')
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        try:
            image = self.unmultiply(image)
        except:
            print('Unmultiply after resizing FAILED!')
        image.save(output_folder + output_file_name, quality=quality, optimize=True)
        return(image)
    

    def cropBatch(self, input_folder=None, output_folder=None,
                  crop_width=None, crop_height=None,
                  number_outputs=False, include_original_name=True,
                  clear_output_folder=False):
        file_count = 0
        # Set input folder
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        # Set output folder
        if output_folder:
            output_folder = self.folder_dict[output_folder]
        else:
            output_folder = self.crop_output_folder
        # Delete output folder
        if clear_output_folder:
            try:
                shutil.rmtree(output_folder)
            except Exception:
                error = Exception
        # Create output folder
        if not(os.path.isdir(output_folder)):
            os.mkdir(output_folder)
        # Crop image files in input folder
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

    def crop(self, image=None, input_file_name=None, input_folder=None,
             crop_width=None, crop_height=None, output_file_name=None):
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
        
    def appendBatch(self, base_image_name, input_folder=None, output_folder=None,
                     added_image_position='top', output_height=None, output_width=None,
                     number_outputs=False, include_original_name=True,
                     clear_output_folder=False):
        file_count = 0
        # Set input folder
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        # Set output folder
        if output_folder:
            output_folder = self.folder_dict[output_folder]
        else:
            output_folder = self.append_output_folder
        # Delete output folder
        if clear_output_folder:
            try:
                shutil.rmtree(output_folder)
            except Exception:
                error = Exception
        # Create output folder
        if not(os.path.isdir(output_folder)):
            os.mkdir(output_folder)
        # append base_image with image files in input folder
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
            appended_image = self.append(base_image_name, file_name, input_folder=input_folder, output_file_name=output_file_name, added_image_position=added_image_position)

    def append(self, base_image_name, added_image_name, input_folder=None, output_folder=None, added_image_position='top', output_file_name='output', output_height=None, output_width=None):
        if not(input_folder):
            input_folder = self.input_folder
        if not(output_folder):
            output_folder = self.append_output_folder
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
        appended_image = Image.new("RGBA", (output_width, output_height))
        appended_image.paste(base_image, (base_image_x, base_image_y), base_image)
        appended_image.paste(added_image, (added_image_x, added_image_y), added_image)
        appended_image.save(output_folder + output_file_name, 'PNG')
        return(appended_image)

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

    def overlay(self, base_image=None, base_image_name=None, added_image=None, added_image_name=None, input_folder=None, output_folder=None, output_file_name='output', auto_resize=False, save_image=True):
        if not(input_folder):
            input_folder = self.input_folder
        if not(output_folder):
            output_folder = self.overlay_output_folder
        if not(base_image):
            base_image = Image.open(input_folder + '/' + base_image_name).convert("RGBA")
        if not(added_image):
            added_image = Image.open(added_image_name).convert("RGBA")
        # ISSUE - resizing removes transparency
        # SOLUTION - use numpy
        # added image is resized if it does not match the base image
        if auto_resize:
            if added_image.width != base_image.width or added_image.height != base_image.height:
                added_image = self.resize(image=added_image, input_file_name=added_image_name, new_width=base_image.width, new_height=base_image.height)
        # images are overlayed
        overlayed_image = Image.new("RGBA", (base_image.width, base_image.height))
        overlayed_image.paste(base_image, (0, 0), base_image)
        overlayed_image.paste(added_image, (0, 0), added_image)
        if save_image:
            if not('.png' in output_file_name):
                output_file_name += '.png'
            overlayed_image.save(output_folder + output_file_name, 'PNG')
        return(overlayed_image)

    def overlayBatch(self, added_image_name, input_folder=None, output_folder=None,
                     number_outputs=False, include_original_name=True, clear_output_folder=False,
                     auto_resize=True):
        file_count = 0
        # Set input folder
        if input_folder:
            input_folder = self.folder_dict[input_folder]
        else:
            input_folder = self.input_folder
        # Set output folder
        if output_folder:
            output_folder = self.folder_dict[output_folder]
        else:
            output_folder = self.overlay_output_folder
        # Delete output folder
        if clear_output_folder:
            try:
                shutil.rmtree(output_folder)
            except Exception:
                error = Exception
        # Create output folder
        if not(os.path.isdir(output_folder)):
            os.mkdir(output_folder)
        # overlay added image on top of image files in input folder
        for base_image_name in os.listdir(input_folder):
            file_count += 1
            output_file_name = ''
            if number_outputs:
                output_file_name = str(file_count)
                if include_original_name:
                    output_file_name += '_' + base_image_name
                else:
                    if not('.png' in output_file_name):
                        output_file_name += '.png'
            if include_original_name:
                output_file_name += base_image_name
            overlayed_image = self.overlay(base_image_name=base_image_name,
                                           added_image_name=added_image_name,
                                           input_folder=input_folder,
                                           output_file_name=output_file_name,
                                           auto_resize=auto_resize)



    def compress(self):
        shit = 'balls'

    def compressBatch(self):
        shit = 'balls'

    def overlayVideo(self, base_image_name, video_name, input_folder=None, output_folder=None, duration=4, added_image_position='top', output_file_name='output', output_height=None, output_width=None):
        video_file = VideoFileClip(video_name)
        image_clip = (ImageClip(base_image_name)
           .set_start(0) #which second to start displaying image
           .set_duration(duration) #how long to display image
           .set_position(("center", "bottom")))
        overlayed_video = CompositeVideoClip([video_file, image_clip])
        overlayed_video.write_videofile(output_file_name + '.mp4', verbose=False, logger=None)


    # NON-FUNCTIONAL
    # This function is meant to allow PIL to resize images while maintaining transparency
    def premultiply(self, image):
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y]
                if a != 255:
                    r = r * a // 255
                    g = g * a // 255
                    b = b * a // 255
                    pixels[x, y] = (r, g, b, a)
        image.pixels = pixels
        return(image)


    # NON-FUNCTIONAL
    # This function is meant to allow PIL to resize images while maintaining transparency
    def unmultiply(self, image):
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y]
                if a != 255 and a != 0:
                    r = 255 if r >= a else 255 * r // a
                    g = 255 if g >= a else 255 * g // a
                    b = 255 if b >= a else 255 * b // a
                    pixels[x, y] = (r, g, b, a)
        image.pixels = pixels
        return(image)

if __name__ == '__main__':
    IT = ImageTools()

## Overlay
    ##IT.overlay(input_folder='inputs', added_image_name='transparent_title.png', base_image_name='evan.png', auto_resize=True)
    ##IT.overlayBatch(input_folder='inputs', added_image_name='transparent_title.png', number_outputs=True, include_original_name=False, clear_output_folder=True)


### Sort
    #IT.sortBatch(input_folder='inputs', clear_output_folder=True)


### Portrait
    IT.resizeBatch(input_folder='portrait_outputs', new_width=930, clear_output_folder=True)
    IT.cropBatch(input_folder='resize_outputs', crop_height=1202, clear_output_folder=True)
    IT.appendBatch(input_folder='crop_outputs', base_image_name='jaeger_bumper.png', number_outputs=True, include_original_name=False, clear_output_folder=True)
##    ##IT.overlayBatch(input_folder='append_outputs', added_image_name='gallery4_portrait_title.png', number_outputs=True, include_original_name=False, clear_output_folder=True, auto_resize=False)
##    ##IT.resizeBatch(input_folder='append_outputs', output_folder='outputs', new_height=693, quality=85, number_outputs=True, include_original_name=False, clear_output_folder=True)


### Landscape
    ##IT.resizeBatch(input_folder='landscape_outputs', new_width=1280, clear_output_folder=True)
    ##IT.cropBatch(input_folder='resize_outputs', crop_height=592, clear_output_folder=True)
    ##IT.appendBatch(input_folder='crop_outputs', base_image_name='landscape_bumper.png', number_outputs=True, include_original_name=False, clear_output_folder=True)
    ####IT.resizeBatch(input_folder='append_outputs', output_folder='outputs', new_height=693, quality=85, number_outputs=True, include_original_name=False, clear_output_folder=True)


### Videos
    IT.overlayVideo(base_image_name='set509_bumper.png', video_name='set509_video.mp4', input_folder='inputs', output_folder='outputs')
    ##>>> myClip.resize(width=800) # height computed automatically.


    ##moviepy.video.fx.all.resize(clip, newsize=None, height=None, width=None, apply_to_mask=True)

    ##    # Import everything needed to edit video clips
    ##from moviepy.editor import *
    ## 
    ### loading video dsa gfg intro video
    ### and getting only first 5 seconds
    ##clip1 = VideoFileClip("dsa_geek.webm").subclip(0, 5)
    ## 
    ### getting width and height of clip 1
    ##w1 = clip1.w
    ##h1 = clip1.h
    ## 
    ##print("Width x Height of clip 1 : ", end = " ")
    ##print(str(w1) + " x ", str(h1))
    ## 
    ##print("---------------------------------------")
    ## 
    ### resizing video downsize 50 % 
    ##clip2 = clip1.resize(0.5)
    ## 
    ### getting width and height of clip 1
    ##w2 = clip2.w
    ##h2 = clip2.h
    ## 
    ##print("Width x Height of clip 2 : ", end = " ")
##print(str(w2) + " x ", str(h2))
