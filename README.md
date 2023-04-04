# Myphysio

## Table of content

1. Introduction 
6. [Reference](#Reference)


## Background:
Structured physical therapy program, such as the one described by Alvarez et al., has been shown to result in successful subjective and functional outcomes for 83% of patients, with 89% reporting satisfaction with their results (Terry Canale, 2013).
This program includes the use of ankle-foot orthoses, high-repetition exercises, plantar flexion activities, and a home exercise program with gastroscopes tendon stretching. Furthermore, task-oriented exercise, such as full body-weight support training, can also improve functional mobility and 6-minute walk performance in stroke patients over a 6-month period, with greater gains seen in the first 3 months (JOEL STEIN, 2009). Conventional rehabilitation care typically leads to a plateau in mobility recovery within 3 months after a stroke, but task-oriented exercise can continue to improve fitness and mobility function for at least 6-months. Thus, studies shows that long-term exercise is recommended for sustained regular exercise to improve fitness and cardiovascular health for all stroke patients. 
Rehabilitation is an important part of tertiary prevention, with the goal of attaining and maintaining the best possible level of functioning for those with illness or disability (Finkelman, 2017 )While rehabilitation should begin on the first day after surgery with a progressive ambulation program (Joel A. DeLisa, 2005), in most cases the physiotherapist will not see the patient through to full recovery (Karen Atkinson, 2005). Therefore, it becomes the responsibility of the patient to further commit to post-rehabilitation exercises.


## Problem Statement:
One of the major challenges faced by patients seeking physiotherapy services is the lack of an alternative and technological approach for online personal assistance. This can lead to problems such as lack of discipline and commitment to post-rehabilitation activities. In addition, there is often a lack of awareness among patients about the importance of physiotherapy exercises, leading to a lack of motivation and compliance with treatment. 
These challenges can hinder the effectiveness of physiotherapy services and can have negative impacts on patient recovering journey. Thus, in this case, we need to develop a framework that suits the patient situation. Foremost, we must evaluate and assess the patient experience after their post-rehabilitation sessions. 


## Model Design:
The collected and augmented data will be used to train and test a convolutional neural network (CNN) model for pose detection. The model will be implemented using Python and the MediaPipe library. The CNN model will consist of multiple convolutional and pooling layers, followed by fully connected layers, designed to extract useful features from the images. ReLU activation function will be used in the hidden layers (Thampi, 2021) to introduce non-linearity in the model. Dropout technique will be used to prevent overfitting (Oliver Duerr, 2020).




![image](https://user-images.githubusercontent.com/63984422/229899316-0442b555-2c89-40ed-bf17-ce946edcc415.png)



## Implementation of the customed CNN (MyPhysio):

The implementation of the proposed algorithm will involve several stages. First, an object detection algorithm will be trained for a specific pose, such as the camel pose. This process will be repeated for multiple poses. Next, the trained algorithms will be matched with specific interfaces that provide instructions for the user to perform the exercise. These interfaces will be separate for each pose. When the user performs the exercise, the algorithm in the backend will compare the user's pose with the already labeled and trained data. The object detection algorithm will then be applied to the new data coming from the user's camera. If the exercise is performed correctly, the system will start counting and provide feedback to the user through sounds, visual cues, and measurements of the angles between the joints.
Experiment and Evaluation:
The performance of the proposed CNN model will be evaluated using standard performance metrics such as accuracy, precision, recall and F1-score. The model will be tested on a separate dataset to ensure unbiased results. The model will be trained and evaluated using k-fold cross-validation technique to make sure that the model is robust enough to generalize to unseen data. 

### Model Deployment:
Upon successful evaluation of the CNN model, it will be deployed for users. The model will be able to assist patients in detecting and correcting improper poses during their rehabilitation exercises, ultimately improving the speed and quality of recovery for individuals undergoing rehabilitation exercises. The model will be integrated with a mobile application which will be accessible to users for monitoring the progress and providing feedback. The deployed model will be continuously updated with new data to improve its performance over time. 

![image](https://user-images.githubusercontent.com/63984422/229899450-31d26569-f8cb-436c-a8ba-5a9aacf12b56.png) <br>
<br>
High Fedality prototype for MyPhysio
<br>
https://www.figma.com/proto/gbZ99dv9uzuMIsDXwAaasf/myphysio?node-id=3%3A2&scaling=scale-down&page-id=0%3A1&starting-point-node-id=3%3A2&show-proto-sidebar=1







## Reference



1. https://www.behance.net/gallery/128749951/Physiologic-Physiotherapist-App-%28iOS-Android%29?tracking_source=search_projects%7Cphysiotherapist

2. https://www.behance.net/gallery/147178079/Alison-Bradfield-Physiotherapy-Brand-Identity-Design?tracking_source=search_projects%7Cphysiotherapist

3. https://www.behance.net/gallery/127217923/UX-Case-Study-Physiotherapy-App-Redesign/modules/721995213

4. http://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/f2016/alp225_eli8_rj245/alp225_eli8_rj245/alp225_eli8_rj245/Website%20Code/alp225_eli8_rj245.html
https://create.arduino.cc/projecthub/gini76/a-posture-detector-sending-bluetooth-data-to-a-cordova-app-36855

5. https://create.arduino.cc/projecthub/postchair-gang/postchair-an-aiot-device-for-bettering-your-posture-6063eb

6. https://makecode.microbit.org/31885-65078-22070-12941
7. https://github.com/akheron/microposture
