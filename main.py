import tkinter
from tkinter import filedialog, messagebox

import PIL
from PIL import Image, ImageTk, ImageDraw, ImageFont




#function that allows checkbox to alter the widget in row 0 column 1 deepending on whether watermark is
#to be text or an image
def switch_widget():

    if checked_state.get() == 1:
        #first delete the stored watermark image path
        img_paths["watermark"] = ["default", "default"]

        #remove current widget in this position
        for widget in frame_2.grid_slaves():
            info = widget.grid_info()
            if info['row'] == 0 and info['column'] == 2:
                widget.grid_remove()

        #also remove the watermark image upload button
        for widget in frame_1.grid_slaves():
            info = widget.grid_info()
            if info['row'] == 1:
                widget.grid_remove()


        #insert Entry widget and Label widget for description of functionality

        #place a new frame (frame3) within column 2 row 0 of frame2 that allows us to arrange label widget and
        # entry widget within it
        frame_3.grid(column=2, row=0)

        # create a 2x1 grid in frame 3
        frame_3.columnconfigure(0, weight=20)
        frame_3.rowconfigure(0, weight=20)
        frame_3.rowconfigure(1, weight=20)

        # now insert the widgets (defined globally)
        input_bar.grid(row=1, column=0)

        description = tkinter.Label(frame_3, text="Enter the text you want to be displayed as a watermark", bg="grey", pady=20)
        description.grid(row=0, column=0)

        # place the button widgets in frame 5
        increase_font_button.grid(row=1, column=0, padx=6)
        reduce_font_button.grid(row=1, column=1, padx=6)




    else:
        #first remove current widget in this position

        for widget in frame_2.grid_slaves():
            info = widget.grid_info()
            if info['row'] == 0 and info['column'] == 2:
                widget.grid_remove()

        #
        # for widget in frame_5.grid_slaves():
        #     info = widget.grid_info()
        #     if info['row'] == 1 and info['column'] == 0:
        #         widget.grid_remove()





        # reinsert watermark image clear canvas
        intitial_wm_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
        intitial_wm_canvas.config(width=200, height=200)
        intitial_wm_canvas.grid(row=0, column=2, pady=50)
        intitial_wm_canvas.create_text(100, 100, text="Watermark Image", font=("Arial", 20), fill="grey")

        #insert the watermark image upload button
        wat_upload_button = tkinter.Button(frame_1, text="Upload Watermark Image", width=20, height=5, command=attach_watermark_file)
        wat_upload_button.grid(row=1)

        # place the change font size button widgets in frame 5
        reduce_font_button.grid(row=1, column=1, padx=6)



def attach_base_file():




    #opens up file dialog to extract the path of the image
    file_path = filedialog.askopenfilename()
    print(file_path)


    # canvas to display uploaded image
    # if file type not an image, catch the exception and run error message box
    try:
        img = Image.open(file_path)

    except PIL.UnidentifiedImageError:
        messagebox.showerror(title="Error", message="File uploaded must be an image")

    else:
        #extract dimensions of image file
        photo_height = img.height
        photo_width = img.width

        print(photo_width)
        print(photo_height)

        #if photo height or width is bigger than 300px, scale the image using pillow's thumbnail()
        #method so it fits within the confines of the canvas (300 x 300)
        if photo_height > 200 or photo_width > 200:

            max_width = 200
            max_height = 200

            img.thumbnail((max_width, max_height), Image.LANCZOS)

            #set new declared height and width for canvas resizing
            photo_height = img.height
            photo_width = img.width

            print(photo_width)
            print(photo_height)





        #this variable is actually not stored properly. Bug exists where Tk essentially discards the reference to the
        #Photoimage after assigment of the variable. Below we will manually keep the reference to this Photoimage object
        #so that it can be displayed on the canvas.
        photoimg = ImageTk.PhotoImage(img)


        #when the photoimage has been successfully chosen, clear the previous Canvas from its position from the grid
        for widget in frame_2.grid_slaves():
            info = widget.grid_info()
            if info['row'] == 0 and info['column'] == 0:
                widget.grid_remove()



        #create canvas instance
        base_img_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
        # resize canvas to fit image dimensions
        base_img_canvas.config(width=200, height=200)


        # before we put our canvas on the grid we can add the Photoimage as an attribute of our canvas object so that python
        #actually keeps the reference to the Photoimage object instead of discarding it.
        base_img_canvas.image = photoimg

        #we can now see the Photoimage when when we use the canvas' .create_image() method with it.
        base_img_canvas.create_image(100, 100, image=photoimg)



        #place our created canvas in the grid
        base_img_canvas.grid(column=0, row=0, pady=50)

        # place image path into path storage dictionary
        img_paths["base"] = file_path


def attach_watermark_file():




    #opens up file dialog to extract the path of the image
    file_path = filedialog.askopenfilename()
    print(file_path)


    # canvas to display uploaded image
    # if file type not an image, catch the exception and run error message box
    try:
        img2 = Image.open(file_path)

    except PIL.UnidentifiedImageError:
        messagebox.showerror(title="Error", message="File uploaded must be an image")

    else:
        #extract dimensions of image file
        photo_height = img2.height
        photo_width = img2.width


        #if photo height or width is bigger than 300px, scale the image using pillow's thumbnail()
        #method so it fits within the confines of the canvas (300 x 300)
        if photo_height > 200 or photo_width > 200:

            max_width = 200
            max_height = 200

            img2.thumbnail((max_width, max_height), Image.LANCZOS)

            #set new declared height and width for canvas resizing
            photo_height = img2.height
            photo_width = img2.width







        #this variable is actually not stored properly. Bug exists where Tk essentially discards the reference to the
        #Photoimage after assigment of the variable. Below we will manually keep the reference to this Photoimage object
        #so that it can be displayed on the canvas.
        photoimg2 = ImageTk.PhotoImage(img2)


        #when the photoimage has been successfully chosen, clear the previous Canvas from its position from the grid
        for widget in frame_2.grid_slaves():
            info = widget.grid_info()
            if info['row'] == 0 and info['column'] == 2:
                widget.grid_remove()



        #create canvas instance
        wm_img_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
        # resize canvas to fit image dimensions
        wm_img_canvas.config(width=200, height=200)


        # before we put our canvas on the grid we can add the Photoimage as an attribute of our canvas object so that python
        #actually keeps the reference to the Photoimage object instead of discarding it.
        wm_img_canvas.image = photoimg2

        #we can now see the Photoimage when when we use the canvas' .create_image() method with it.
        wm_img_canvas.create_image(100, 100, image=photoimg2)



        #place our created canvas in the grid
        wm_img_canvas.grid(column=2, row=0, pady=50)

        #place image path and dimensions into path storage dictionary
        img_paths["watermark"][0] = file_path
        img_paths["watermark"][1] = (img2.width, img2.height)

        print(img_paths["watermark"][1])



#function takes in a font size/logo scale factor, and if watermark creation process is text-based, this argument will be the default font size
#font-size-change buttons will call one of the font change functions that eventually calls this function but first alters the
# input font size by changing the value in the img_paths dictionary.

#Function places the resultant watermarked Pillow Image object in the img_paths dictionary and referes to it in the
#dictionary to render it on the UI. This way the rendering process is dynamic, refreshing whenever this function is called
def process_images(font_size, scale_factor):



    #if there is no base image show no 'no base image' error
    if img_paths["base"] == "default":
        messagebox.showerror(title="No Base Image", message="No base image detected")


    else:



        #check if the checkbutton is checked. If so, implies that watermark is in text form. Process the watermark text
        #and transfer to base image
        if checked_state.get() == 1:




            base_path = img_paths["base"]
            base_image = Image.open(base_path)
            base_image = base_image.convert("RGBA")


            # if the font size passed in is the default value, it implies this function was called from the 'Generate Final Image'
            # button, therefore reset img_paths dictionary's font to original value to avoid the font increase/decrease
            # functionaity skipping sizes.
            if font_size == 80:
                img_paths["font size"] = 80



            #create the watermark layer image that will be placed over the base once wtaermark processed on it
            layer_img = Image.new(mode="RGBA", size=base_image.size, color=(0,0,0,0))

            #create a draw object for the base image
            draw = ImageDraw.Draw(layer_img)


            #load a pillow Imagefont object
            font = ImageFont.truetype("Arial Bold.ttf", font_size)

            #define watermark text
            watermark_text = input_bar.get()



            # calculate the position needed to place the bounding box at the centre of the image
            image_width = layer_img.width
            image_height = layer_img.height

            #calcuate text size through the dimensions of the textbox
            #By putting the (0,0), youre asking Pillow to calculate the bounding box of the text as if it were in
            #the top-left corner of the image
            bbox = draw.textbbox((0, 0), text=watermark_text, font=font)

            # the textbbox variable consists of a tuple (left_edge, top_edge, right_edge, bottom_edge)
            textbox_width = bbox[2] - bbox[0]
            textbox_height = bbox[3] - bbox[1]

            #if textbox width is greater than the base image width, reduce font to half of the size to increase
            #chance of text fitting
            if textbox_width > base_image.width:
                #redefine the font and textbox
                font = ImageFont.truetype("Arial Bold.ttf", font_size * 1 / 2)
                bbox = draw.textbbox((0, 0), text=watermark_text, font=font)
                textbox_width = bbox[2] - bbox[0]
                textbox_height = bbox[3] - bbox[1]





            #set the text colour & transparency: semi-transparent black
            fill_colour = (0, 0, 0, 90)

            #draw the watermark text onto the base image.
            #coordinates will depend on if 'center placement' or 'corner placement' radio button is selected

            if radio_state.get() == 1: #corresponding to 'center placement' radio button selected
                draw.text((image_width-textbox_width - 20, image_height-textbox_height - 20), watermark_text,
                          fill=fill_colour, font=font)
            elif radio_state.get() == 0: #corresponding to 'corner placement' radio button selected
                draw.text((image_width//2-textbox_width//2, image_height//2-textbox_height//2), watermark_text,
                          fill=fill_colour, font=font)



            #add watermark to image with Image object's .alpha_composite() method
            base_image.alpha_composite(layer_img)



            #store the base Image object in the img_paths dictionary
            img_paths["image"] = base_image

            #render the resultant watermarked image in the UI
            render_result()

            print(img_paths["image"])











        #otherwise we will be handling png files

        else:
            # if the font size passed in is the default value, it implies this function was called from the 'Generate Final Image'
            # button, therefore reset img_paths dictionary's font to original value to avoid the font increase/decrease
            # functionaity skipping sizes
            if scale_factor == 1:
                img_paths["logo scale factor"] = 1

            #if there's no watermark image, don't bother asking about all the input requests and png image processing
            #tasks
            if img_paths["watermark"] != ["default", "default"]:

                #extract image paths
                base_path = img_paths["base"]
                watermark_path = img_paths["watermark"][0]

                #load the watermark image and base image and ensure both are 'RGBA' mode to support the png functionality
                wm_image = Image.open(watermark_path)
                base_image = Image.open(base_path)

                wm_image = wm_image.convert("RGBA")
                base_image = base_image.convert("RGBA")

                if base_image.height > 2000 or base_image.width > 2000:
                    scale_factor = scale_factor * 8




                #create_image_watermark and reduce/increase by specified scale factor of the size rendered in window
                #(with .thumbnail() to scale down proportionally)

                wm_desired_width = float(img_paths["watermark"][1][0]) * float(scale_factor)
                wm_desired_height = float(img_paths["watermark"][1][1]) * float(scale_factor)
                size = (int(wm_desired_width), int(wm_desired_height))
                wm_image = wm_image.resize(size)



                #to ensure png is placed right at the bottom corner, subtract minimized img width from base image width and
                #use the result as the paste function x coordinate, and subtract minimzed img height from base image height and use
                #as the paste function y coordinate

                #if the radio box is on 'center' then the x and y coordinates will represent the centre and if the
                #radio box is on 'corner' then the coordinates will represent the corner

                if radio_state.get() == 1:
                    x_cor = int(base_image.width - wm_desired_width)
                    y_cor = int(base_image.height - wm_desired_height)

                elif radio_state.get() == 0:

                    x_cor = int(base_image.width//2 - wm_desired_width//2)
                    y_cor = int(base_image.height//2 - wm_desired_height//2)


                #catch 'ValueError' exception that's returned when non-png file is uploaded

                try:
                    #code below alters watermark transparency

                    alpha = 0.5

                    #create alpha mask: The point(lambda p: p * alpha) function multiplies each pixel's alpha value by the desired transparency level
                    alpha_mask = wm_image.split()[3].point(lambda p: p * alpha)

                    #apply the alpha mask to our watermark image
                    wm_image.putalpha(alpha_mask)


                    # paste watermark image onto original image. Argument structure below ensures that png background is transparent
                    base_image.paste(wm_image, (x_cor, y_cor), wm_image)

                except ValueError:
                    messagebox.showerror(title="Error", message="wrong file format")

                else:

                    #insert resultant base image into img_paths dictionary
                    img_paths["image"] = base_image

                    #render the result image in the UI
                    render_result()

                    print(f"png width: {wm_desired_width}")
                    print(f"png height: {wm_desired_height}")


            #if there is no uploaded watermark image
            else:

                base_path = img_paths["base"]
                base_image = Image.open(base_path)
                base_image = base_image.convert("RGBA")

                # insert resultant base image into img_paths dictionary
                img_paths["image"] = base_image

                # render the result image in the UI
                render_result()





def font_increase():
    #increase the font & scale factor in the img_paths dictionary by 30%
    img_paths["font size"] *= 1.3
    img_paths["logo scale factor"] *= 1.3


    #call the process_images() function, inputting the new font size
    process_images(img_paths["font size"], img_paths["logo scale factor"])


def font_decrease():
    # reduce the font & scale factor in the img_paths dictionary by 30%
    img_paths["font size"] *= 0.7
    img_paths["logo scale factor"] *= 0.7

    # call the process_images() function, inputting the new font size
    process_images(img_paths["font size"], img_paths["logo scale factor"])


def render_result():
    #extract a copy the resultant watermarked image object.
    #otherwise function will be altering that same object
    result_img = img_paths["image"].copy()

    # extract dimensions of image file
    photo_height = result_img.height
    photo_width = result_img.width


    # if photo height or width is bigger than 300px, scale the image using pillow's thumbnail()
    # method so it fits within the confines of the canvas (300 x 300)
    if photo_height > 300 or photo_width > 300:
        max_width = 300
        max_height = 300

        result_img.thumbnail((max_width, max_height), Image.LANCZOS)


        # set new declared height and width for canvas resizing
        photo_height = result_img.height
        photo_width = result_img.width

        print(photo_width)
        print(photo_height)

    # this variable is actually not stored properly. Bug exists where Tk essentially discards the reference to the
    # Photoimage after assigment of the variable. Below we will manually keep the reference to this Photoimage object
    # so that it can be displayed on the canvas.
    photoimg = ImageTk.PhotoImage(result_img)

    # when the photoimage has been successfully chosen, clear the previous Canvas from its position from the grid
    for widget in frame_2.grid_slaves():
        info = widget.grid_info()
        if info['row'] == 2 and info['column'] == 1:
            widget.grid_remove()

    # create canvas instance
    result_img_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
    # resize canvas to fit image dimensions
    result_img_canvas.config(width=300, height=300)

    # before we put our canvas on the grid we can add the Photoimage as an attribute of our canvas object so that python
    # actually keeps the reference to the Photoimage object instead of discarding it.
    result_img_canvas.image = photoimg

    # we can now see the Photoimage when we use the canvas' .create_image() method with it.
    result_img_canvas.create_image(150, 150, image=photoimg)

    # place our created canvas in the grid
    result_img_canvas.grid(column=1, row=2, pady=50)


#function where UI responds to center/corner placement radio button switches instantly
def radio_response():
    #as long as there's a base image, when this radio button is clicked process the uploaded images
    if img_paths["base"] != "default" and img_paths["image"] != "default":
        process_images(img_paths["font size"], img_paths["logo scale factor"])


def clear_images():


    #clear the canvas widgets

    for widget in frame_2.grid_slaves():
        info = widget.grid_info()
        if info['row'] == 0 and info['column'] == 0:
            widget.grid_remove()

        #only remove top right widget if not in text mode, otherwise keep input bar upon reset
        if checked_state.get() == 0:
            if info['row'] == 0 and info['column'] == 2:
                widget.grid_remove()

        if info['row'] == 2 and info['column'] == 1:
            widget.grid_remove()



    #ensure the global img_paths variable is what is being reset, not a local variable created in this function
    global img_paths

    img_paths = {"base": "default",
                 "watermark": ["default", "default"],
                 "text": "default",
                 "font size": 80,
                 "logo scale factor": 1,
                 "image": "default"}

    #uncheck the 'Text Mode' check box



    #reset the displayed canvases
    intitial_base_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
    intitial_base_canvas.config(width=200, height=200)
    intitial_base_canvas.grid(row=0, column=0, pady=50)
    intitial_base_canvas.create_text(100, 100, text="Base Image", font=("Arial", 20), fill="grey")

    #render the empty watermark display canvas if text mode is off
    if checked_state.get() == 0:
        intitial_wm_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
        intitial_wm_canvas.config(width=200, height=200)
        intitial_wm_canvas.grid(row=0, column=2, pady=50)
        intitial_wm_canvas.create_text(100, 100, text="Watermark Image", font=("Arial", 20), fill="grey")

    intitial_fin_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
    intitial_fin_canvas.config(width=300, height=300)
    intitial_fin_canvas.grid(row=2, column=1, pady=50)
    intitial_fin_canvas.create_text(150, 150, text="Result", font=("Arial", 20), fill="grey")


def save_result():

    #ensure there is a base image

    #if there is no base image show no 'no base image' error
    if img_paths["base"] == "default":
        messagebox.showerror(title="No Base Image", message="No base image detected")

    else:
        #ensure there is a result image displayed
        if img_paths["image"] == "default":
            messagebox.showerror(title="No result", message="Please generate a result")

        else:


            #get copy of image object
            img_copy = img_paths["image"].copy()

            #convert to JPEG
            img_copy = img_copy.convert("RGB")

            #get path to downloads folder

            save_path = filedialog.asksaveasfilename(defaultextension=".jpeg")
            # downloads_directory = "/Users/alexsokefun/Downloads"



            #save to downloads
            img_copy.save(save_path)




##### MAIN UI SETUP ###########



#global variable that will store the paths of the selected base and watermark images. Initialised with
#default strings which will be replaced upon photo selection function calling.
#watermark dictionary entry will be a list composed of a string for the path entry, and a tuple of the image dimensions
#for reference when maintaining aspect ratio when resizing,
img_paths = {"base": "default",
             "watermark": ["default", "default"],
             "text": "default",
             "font size": 80,
             "logo scale factor": 1,
             "image": "default"}



#generate our window
window = tkinter.Tk()

#set window title
window.title("Watermark Generator")

#set default size of window
window.minsize(width=1300, height=500)


#define a left frame (for our buttons) and a right frame (to display the image we're editing
frame_1 = tkinter.Frame(window, width=300, height=500)
#edit frame colour
frame_1.config(bg="red")
#we place it in our window using the 'pack' configuration
frame_1.pack(side='left', fill='y')

frame_2 = tkinter.Frame(window, width=700, height=500)
frame_2.config(bg="grey")
frame_2.pack(side='left', expand=True, fill='both')


#define a grid within frame_1 (1x4)

frame_1.rowconfigure(0, weight=20)
frame_1.rowconfigure(1, weight=20)
frame_1.rowconfigure(2, weight=20)
frame_1.rowconfigure(3, weight=20)


#define a grid within frame 2 (3x3)
frame_2.columnconfigure(0, weight=20)
frame_2.columnconfigure(1, weight=20)
frame_2.columnconfigure(2, weight=20)

frame_2.rowconfigure(0, weight=20)
frame_2.rowconfigure(1, weight=20)
frame_2.rowconfigure(3, weight=20)

#define frame_3 within column 2 row 0 of frame2 that allows us to arrange label widget and entry widget within it
#when they are rendered in response to 'Text Mode' check button
frame_3 = tkinter.Frame(frame_2, bg="grey")

#define a 3x1 grid within column 0 row 2 of frame 1
frame_4 = tkinter.Frame(frame_1, bg='grey')
frame_4.grid(column=0, row=3)
frame_4.columnconfigure(0, weight=20)
frame_4.rowconfigure(0, weight=20)
frame_4.rowconfigure(1, weight=20)
frame_4.rowconfigure(2, weight=20)

#define a 2x2 grid within column 0 row 1 of frame 2
frame_5 = tkinter.Frame(frame_2,bg="grey")
frame_5.rowconfigure(0, weight=20)
frame_5.rowconfigure(1, weight=20)
frame_5.columnconfigure(0, weight=20)
frame_5.columnconfigure(1, weight=20)



#increase/reduce font size buttons that will be rendered in frame 5 in response to 'Text Mode' Check button
increase_font_button = tkinter.Button(frame_5, text="Increase Font Size", command=font_increase, bg='grey', height=2)
reduce_font_button = tkinter.Button(frame_5, text="Reduce Font Size", command=font_decrease, bg='grey',height=2)

# place frame 5 within frame 2 column 0 row 1 and insert increase/reduce font size buttons
frame_5.grid(column=0, row=1)
# place the button widgets in frame 5
increase_font_button.grid(row=1, column=0, padx=6)
reduce_font_button.grid(row=1, column=1, padx=6)

#Checkbutton widget that allows the widget in row 2, column 2 to change between text input bar and watermark image space
# display. This widget also toggles the presence of the 'Upload watermark image' button
checked_state = tkinter.IntVar()
check_button = tkinter.Checkbutton(frame_2, text="Text Mode", variable=checked_state, command=switch_widget, bg='grey')
checked_state.get()
check_button.grid(row=0, column=1)


#Radiobuttons that allow user to specify if watermark should be placed at center or corner of image
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(frame_4, text="centre placement", variable=radio_state, value=0,
                                    command=radio_response, bg="red", fg='white')
radio_button2 = tkinter.Radiobutton(frame_4, text="corner placement", variable=radio_state, value=1,
                                    command=radio_response, bg="red", fg='white')
radio_button1.grid(column=0, row=1)
radio_button2.grid(column=0, row=2)


#base image upload button
base_upload_button = tkinter.Button(frame_1, text='Upload Base Image', width=20, height=5, command=attach_base_file)
base_upload_button.grid(row=0, padx=15)


#watermark image upload button
wat_upload_button = tkinter.Button(frame_1, text="Upload Watermark Logo", width=20, height=5, command=attach_watermark_file)
wat_upload_button.grid(row=1, padx=15)

#Generate button
generate_button = tkinter.Button(frame_2, text="Generate Final Image", width=15, height=3, padx=5, pady=5,
                                 command=lambda: process_images(80, 1))
generate_button.grid(row=2, column=2)



#reset button
reset_button = tkinter.Button(frame_1, text="Clear All", width=20, height=5, command=clear_images)
reset_button.grid(row=2, padx=15)


#base image clear canvas
intitial_base_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
intitial_base_canvas.config(width=200, height=200)
intitial_base_canvas.grid(row=0, column=0, pady=50)
intitial_base_canvas.create_text(100, 100, text="Base Image", font=("Arial", 20), fill="grey")



#watermark image clear canvas
intitial_wm_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
intitial_wm_canvas.config(width=200, height=200)
intitial_wm_canvas.grid(row=0, column=2, pady=50)
intitial_wm_canvas.create_text(100, 100, text="Watermark Image", font=("Arial", 20), fill="grey")




#final image clear canvas
intitial_fin_canvas = tkinter.Canvas(frame_2, highlightthickness=3, highlightbackground="black")
intitial_fin_canvas.config(width=300, height=300)
intitial_fin_canvas.grid(row=2, column=1, pady=50)
intitial_fin_canvas.create_text(150, 150, text="Result", font=("Arial", 20), fill="grey")

#save button
save_button = tkinter.Button(frame_2, text="Save Image", highlightthickness=3, highlightbackground="red",
                             command=save_result)
save_button.config(height=5, width=7)
save_button.grid(row=2, column=0)




#Entry widget for watermark text input
input_bar = tkinter.Entry(frame_3, width=30)




#keep our window open
tkinter.mainloop()