<iframe width="560" height="315" src="https://www.youtube.com/watch?v=eiyIssjg2K0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# smartsortr (TurtleHacks 2023 Submission)

## Inspiration
We've all seen people throwing their trash in the recycling and vice-versa, and it happens so commonly that our recycling processes have become very inefficient. Whether this is because people don't know where their waste should go, or don't want to spend the time to find out what the proper disposal method is, we have created a simple solution that will make recycling easier for anyone!
## What it does
We've essentially created a small hardware unit including a camera with an LED output, which uses the power of machine learning to detect what someone is going to throw in the garbage or recycling. Our unit will recognize objects through a camera, and simply tell a person in front of the bin where their waste should go.
## How we built it
We had two main approaches to this problem, the first was training our own model, and the second using external API's. When training our own model, we used the built-in functionality of TensorFlow to train a CNN off of our own images of garbage or recycling, as well as images off of the internet. We used [labelimg](https://github.com/heartexlabs/labelImg) for annotation of the training set, and OpenCV for image preprocessing of the captured photos. On the second approach which came a lot easier, we use OpenCV for the image preprocessing and then call the [Mantis Object Detection API](https://rapidapi.com/ja/mantis-object-detection-mantis-object-detection-default/api/mantis-object-detection/) via ResNet-50 to return an accurate object detection, which then determines how we will interact with the hardware. For example, if our system detects a plastic bottle, our LED will quickly tell the user to throw the bottle in the recycling bin.
## Challenges we ran into
Initially, we began building our own CNN to to detect objects in real time, but we quickly realized this was going to be over-complicated and given our time constraints, we began looking for pre-made models. Our first attempt at using a pre-built model with our own training data was working, but the model was not particularly fast, which was quite important for our device given hardware limitations. In the end, we ended up going with an API solution for object detection, as it was the easiest and most accurate approach, while still being relatively fast.
## Accomplishments that we're proud of
During our hacking day on Saturday, we learned a lot about computer vision, and how useful it can be to solve real world problems. We got lots of experience with Tensorflow/Keras, and OpenCV, as well as learning about how to interact with a Raspberry Pi on the hardware side. We are proud to have created a working prototype, and though there is lots to improve upon, it looks to be a promising environmental solution for waste sorting.
## What we learned
During the hackathon, we learned how to work as a team and delegate tasks effectively. We also gained lots of technical experience across Python, TensorFlow, OpenCV, working with APIs, and hardware.
## What's next for SmartSortr
The system we've came up with seems to be a basic, cheap, and scalable solution for the waste sorting problem, but there are of course many challenges and knacks to work through. Here are a couple things we have in mind:

- It may be best to employ this solution in a waste sorting facility as opposed to at the bin itself, since there can be errors with the device, and people may still choose to ignore it. 
- There an inherent issue with a strictly an image input, as the model will not be able to detect composition of the material, which is an important part in waste sorting.

On a large scale, we would need to build a custom model with a much more accurate object detector, as API calls will get expensive quickly. We would also be using cheaper harder, likely a custom designed PCB with a cheaper camera unit.

Overall we had a great time at TurtleHacks, and learned a lot! Thank you to the organizers, and best of luck to all the competitors!

## Why is there only one file here?

Git LFS isn't being nice to me and I'm getting pretty tired (its 4am) so I've uploaded the custom model here: https://drive.google.com/drive/folders/1ymgEhrelzn36dccISq2G5YpCx66Ghs-P?usp=sharing
