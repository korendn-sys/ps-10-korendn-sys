import matplotlib.pyplot as plt

# 1. Image loading is already done in cell _7_oa1WvE1RO, result is `img_array`
# For convenience, let's ensure we have img_array from the previous step
# If this cell is run independently, you might need to re-run the previous cell

# 2. Suppress noise using a median filter
# The edge_detection function expects a 3-channel image, but median works on grayscale too.
# For noise suppression before edge detection, we can apply it on the color image first.
clean_image = median(img_array, ball(3))

# 3. Run the noise-free image through the `edge_detection` function
edge_mag_image = edge_detection(clean_image)

# 4. Convert the resulting edgeMAG array into a binary array
# To choose a threshold, let's look at the histogram of edge_mag_image
plt.hist(edge_mag_image.ravel(), bins=50)
plt.title('Histogram of Edge Magnitudes')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.show()

# Based on the histogram, choose a threshold (this might need adjustment after seeing the plot)
# For demonstration, let's pick a value. User can adjust this.
threshold = 50 # This value might need to be adjusted after viewing the histogram
edge_binary = edge_mag_image > threshold

# 5. Display the binary image and save it
# Convert boolean array to uint8 for saving, typically 255 for True, 0 for False
edge_binary_display = (edge_binary * 255).astype(np.uint8)

edge_image = Image.fromarray(edge_binary_display)

plt.imshow(edge_image, cmap='gray')
plt.title('Binary Edge-Detected Image')
plt.axis('off')
plt.show()

edge_image.save('my_edges.png')
print("Edge-detected image saved as 'my_edges.png'")
