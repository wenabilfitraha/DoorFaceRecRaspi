import cv2
import setup
import face
import InOut

from time import sleep

if __name__ == '__main__':
    # Move box to locked position.
    InOut.servo.max()
    sleep(0.1)
    InOut.led_red.on()
    # Load training data into model.
    print('Loading training data...')
    model = cv2.face.EigenFaceRecognizer_create()
    model.read(setup.TRAINING_FILE)
    print('Training data loaded!')
    # Initialize camera
    camera = setup.get_camera()
    print('Running box...')
    print('Press button to lock (if unlocked), or unlock if the correct face is detected.')
    print('Press Ctrl-C to quit.')
    while True:
        # TODO: Check if button is pressed.
        if InOut.cam_unlock.is_pressed:
            InOut.led_grn.blink()
            print('Button pressed, looking for face...')
            # Check for the positive face and unlock if found.
            image = camera.read()
            # Convert image to grayscale.
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            # Get coordinates of single face in captured image.
            result = face.detect_single(image)
            if result is None:
                print('Could not detect single face!  Check the image in capture.pgm' \
                    ' to see what was captured and try again with only one face visible.')
                InOut.led_grn.off()
                continue
            x, y, w, h = result
            # Crop and resize image to face.
            crop = face.resize(face.crop(image, x, y, w, h))
            # Test face against model.
            label, confidence = model.predict(crop)
            print('Predicted {0} face with confidence {1} (lower is more confident).'.format(
                'POSITIVE' if label == setup.POSITIVE_LABEL else 'NEGATIVE', 
                confidence))
            if label == setup.POSITIVE_LABEL and confidence < setup.POSITIVE_THRESHOLD:
                print('Recognized face!')
                InOut.servo.min()
                sleep(0.1)
                InOut.led_grn.on()
                InOut.led_red.off()
            else:
                print('Did not recognize face!')
        if InOut.cam_lock.is_pressed:
            print('Locking the door!')
            InOut.servo.max()
            sleep(0.1)
            InOut.led_grn.off()
            InOut.led_red.on()
            #pause()
        if InOut.unlock.is_pressed:
            print('Open door lock from inside!')
            InOut.servo.min()
            sleep(0.1)
            InOut.led_grn.on()
            InOut.led_red.off()
            #pause()
        if InOut.lock.is_pressed:
            print('Locking the door from inside!!')
            InOut.servo.max()
            sleep(0.1)
            InOut.led_grn.off()
            InOut.led_red.on()
            #pause()