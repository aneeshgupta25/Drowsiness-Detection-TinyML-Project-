# Drowsiness-Detection-TinyML-Project-

Long-distance travellers, particularly truck drivers, bus drivers, and taxi drivers, often face extended hours of driving, making them susceptible to sleep deprivation. The associated risks of fatigue and drowsiness can significantly compromise a driver's reaction time, attention, and overall ability to safely operate a vehicle. According to the National Safety Council (NSC), drowsy driving contributes to approximately 100,000 crashes, 71,000 injuries, and 1,550 fatalities annually. The prevalence of drowsy driving poses a substantial threat to road safety. The consequences of fatigue-related accidents underscore the urgent need for proactive measures to detect and mitigate driver drowsiness. 

In response to this challenge, we propose the development of a `Drowsiness Detection System` that leverages image processing and machine learning techniques to alert drivers when signs of fatigue become apparent.

Using Python libraries such as ***OpenCV*** for image processing and ***Keras*** for model development, the project utilizes Convolutional Neural Networks (CNNs) for classification, training the model on a dataset containing 2900 images of both alert and drowsy drivers. Images captured from a webcam are preprocessed and fed into the CNN to determine the state of the driver's eyes. Key steps include face detection using the Haar Cascade Classifier, defining a Region of Interest (ROI), identifying the eyes within the ROI, and classifying them as open or closed. A drowsiness score is then calculated based on the duration of eye closure, triggering an alarm if the driver appears sleepy, providing a proactive approach to mitigate the risks associated with drowsy driving.

## Project Features:
1. **Eye State Monitoring**: Monitoring the state of the driver's eyes is a fundamental feature. This involves detecting factors like eyelid closure. For example, heavy eyelids or prolonged periods with closed eyes can indicate drowsiness.
2. **Machine Learning Models**: Utilizing machine learning models such as CNN trained on labeled datasets can effectively combine multiple features and patterns to accurately predict the driver's drowsiness state.
3. **Real-time Alerts and Interventions**: Implementing real-time alerts or interventions (i.e., audible alerts, seat vibrations) when drowsiness is detected can help mitigate the risk of accidents by alerting the driver or triggering automated safety systems.
   
## Limitations of the project:
1. **Determining the Optimum Threshold**: We need to determine the threshold score that is appropriate for the application for timely alerts and minimizing false alarms. This score is dependent upon the real time application the system is being used for and needs to take into considerattion specific environment and driver features.
2. **Dataset Robustness**: Despite using a large dataset of images, the model's accuracy can be further improved by addition of more data points that portray a wide variety of situation. We may also consider training the model on images specific to the driver and the environment the system will be used in.
3. **Ambient Lighting**: The accuracy of classification is also dependent upon environmental factors like lighting conditions.

## Future Work:
1. Dataset can be made more robust by using data augmentation techniques. We can also gather more data which portrays different environmental conditions to ensure that the model works well in varied conditions. We can conduct a training exercise with specific drivers in order to tune our model to specific user characteristics.
2. Ambient Lighting can be addressed by the inclusion of night mode which allows the sensor to let in more light allowing for brighter and clearer pictures even in the dark.
3. If the driver does not respond even after continuous ringing of the alarm, we can connect the driver drowsiness detection system to an automatic braking system or use smart seats that can start vibrating to wake the driver up.
