import matplotlib.pyplot as plt


clean_image = median(img_array, ball(3))

edge_mag_image = edge_detection(clean_image)

plt.hist(edge_mag_image.ravel(), bins=50)
plt.title('Histogram of Edge Magnitudes')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.show()

threshold = 50 
edge_binary = edge_mag_image > threshold

edge_binary_display = (edge_binary * 255).astype(np.uint8)

edge_image = Image.fromarray(edge_binary_display)

plt.imshow(edge_image, cmap='gray')
plt.title('Binary Edge-Detected Image')
plt.axis('off')
plt.show()

edge_image.save('my_edges.png')
print("Edge-detected image saved as 'my_edges.png'")
