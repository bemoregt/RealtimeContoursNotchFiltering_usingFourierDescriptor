# Real-time Contour Notch Filtering using Fourier Descriptors

This application demonstrates real-time contour shape manipulation using Fourier Descriptors and notch filtering. The interactive GUI allows users to dynamically modify contour shapes by filtering specific frequency components in the Fourier domain.

## Features

- Image contour extraction and visualization
- Fourier Descriptor computation for contour representation
- Real-time notch filtering with interactive control
- Split-view display showing original vs. filtered contours

## How It Works

### Fourier Descriptors

Fourier Descriptors are a powerful method for shape analysis and representation that:

1. Converts a closed contour into a sequence of complex numbers (x + jy)
2. Applies Fourier Transform to this sequence
3. Results in frequency components that encode shape information:
   - Low frequencies → Overall shape
   - Middle frequencies → Primary features
   - High frequencies → Fine details and noise

### Notch Filtering

This application implements notch filtering in the frequency domain, which:

- Selectively removes specific frequency components
- Preserves the remaining shape information
- Enables controlled shape modification

The interactive interface allows you to:
- View the original shape on the left
- See the filtered result on the right
- Adjust the notch frequency by moving your mouse

## Technical Implementation

The code performs the following steps:

1. Loads an image and extracts contours using OpenCV
2. Converts contours to complex form (x + jy)
3. Computes Fourier descriptors using FFT
4. Applies notch filtering to remove selected frequency components
5. Performs inverse FFT to reconstruct the modified contour
6. Visualizes both original and filtered contours in real-time

## Dependencies

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- Tkinter

## Usage

1. Install the required dependencies:
   ```
   pip install opencv-python numpy matplotlib
   ```

2. Update the image path in the script to point to your test image:
   ```python
   image_path = "your_image.jpg"  # Change this to your image path
   ```

3. Run the application:
   ```
   python notch_filter_gui.py
   ```

4. Move your mouse horizontally across the plot to change the notch filter frequency.

## Applications

This technique has applications in:

- Computer vision and shape analysis
- Pattern recognition
- Image processing
- Shape smoothing and noise removal
- Feature extraction
- Shape morphing and manipulation

## Example Output

When you run the application, you'll see:
- Left panel: Original contours (blue)
- Right panel: Filtered contours (red)
- Top display: Current notch frequency value

The shape will change in real-time as you move your mouse to adjust the filtering.

## License

MIT

## Author

Originally created by @bemoregt