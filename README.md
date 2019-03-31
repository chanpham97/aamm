# Abstract Art Music Matcher

## Phenomena to be Investigated

Our project is an investigation of music's ability to amplify the sentiment of an abstract artwork. 
We are interested in investigating two phenomena:
1. We are interested in the use of features such as color and texture for effective sentiment analysis of abstract artwork. 
2. We are interested in evaluating the effectiveness of music and art pairing to convey a sentiment. 
Our broader goal through this project is to make abstract art more accessible to general public by making generally high-brow abstract art space more tangible 
through the more colloquial musical space. 
We hope to produce results illustrating that color and texture-based visual sentiment analysis can achieve high faithfulness to human sentiment classification. 

In devising our methods, we consider the following previous works:
1. Researchers Yanulevskaya and Uijlings identified a correlation between the brightness of colors and humans' sentiment tagging of abstract artworks [1]. 
They also found that human subjects with high variance in art expertise identified similar emotions in paintings, an insight that will prove interesting in our user evaluation phase. 
2. We are influenced by Paul Sylvia's arousal and appraisal models of emotion detection, which we discuss further in the Limits section of this proposal [2]. 
3. We find that much of the work in visual sentiment analysis of abstract and face-less images revolves around supervised machine learning algorithms and very deep neural networks, 
such as presented in Islam and Zhang's work [5]. 

While we are incorporating insights from previous works, we believe there is strong potential to deviate from previous research in one important way: we aim to create a more simple, human-understandable visual sentiment classification algorithm (rather than embedded representations, using human-identifiable features like color and texture) and try to achieve reasonably high accuracy.

## Limits on the Investigation
For optimal results within the limited time frame, we will be limiting several features of the project. 
1. As the project aims to connect users to art they may struggle to otherwise understand, we will focus specifically on abstract art for sentiment tagging. 
Within that space, we will select a handful of artists to create more similarity between art pieces for better sentiment matching.
2. Since our sentiment analysis is based on colors and shapes, we will only be selecting art pieces with color (i.e. not black and white) and no faces or objects. 
Due to this, we will not be able to use face sentiment analysis tagging or object-recognition tagging, which is attempted in other art sentiment analysis research 
(e.g. https://www.aclweb.org/anthology/R15-1035) and may have added more reference points for sentiment analysis.
3. Another potential limitation is due to the separation of arousal versus appraisal emotion models, as explored by Sylvia [2]. 
These arousal model identifies whether emotion is evoked and the appraisal model identifies which emotions are evoked. 
While certain features have been studied and shown to evoke interest and emotion, there is still little research on specific emotions induced by art under the newer appraisal emotion model.  
Due to this, it is possible that we may only be able to identify whether music amplifies emotional arousal, a generalization of the original goal of specific emotional arousal.
4. In terms of music, the categories will be static with sentiment analysis done by external APIs (e.g. Spotify). As music sentiment analysis is well researched and non-visual, 
it will not be a focus point in the project. Due to this, we are relying on Spotify's tagging and not developing our own. The crux of our project is visual semantic analysis of the abstract artworks.
5. User testing and thus algorithm revisions will be based on Columbia students, potentially affecting results due to particular age range, background, and education level.

## Anticipated Methods and Results

This section of our proposal offers a brief step-by-step plan for the development of our final product and a more detailed discussion of the features we will use for sentiment analysis of abstract art. 
Our final product is a web application: a virtual art gallery where every painting is viewed while listening to a corresponding piece of instrumental music. 

### Steps
1. We first assemble our visual database, a subset of the WikiArt database of artworks. Our visual database will consist of approximately 1000 images of paintings that are in color and not portraits.
2. Next, we assemble music playlists for each sentiment using Spotify. This assembly of our music database will be done through manual selection.
3. We write our program to determine each painting's sentiment. This is a classification algorithm based on features we will discuss below: represented colors, number of colors, color contrast, color darkness, and sharpness of transitions between colors.
4. We extend our program to map art to music, based on sentiment. Likely, we will have a distinct playlist for each sentiment and choose a song randomly from the playlist that corresponds with the sentiment of the painting.
5. Our web application will have two modes: feedback mode and experience mode. The experience mode displays a painting while playing our chosen corresponding music and allows the user to click one button to continue to the next painting and another to exit the experience. The feedback mode contains this functionality with a couple additions. There are thumbs up and thumbs down buttons to evaluate the initial music pairing. This data will be collected on the backend to see which pairings receive what approvals. In this step, we only build feedback mode.
6. We gather people for user testing, gathering qualitative feedback and testing with feedback mode. We also plan to send around a Google Form to evaluate a random sample of pairings.
7. We revise our artwork-music pairing algorithm based on user feedback. We also revise our UI based on qualitative user feedback.
8. We have a second round of user testing to collect data and see if there is improvement in scores.
9. We create the final experience mode without the extra bells and whistles that are in feedback mode. The final UI is finished.

### Features
As mentioned above, the features for sentiment analysis of abstract art we will try to use are represented colors, number of colors, color contrast, color darkness, and saturation of present colors.
1. Colors present: The represented colors are considered based on color theory, which associates different colors with different feelings. 
One such study is presented in the paper, "In the Eye of the Beholder: Employing Statistical Analysis and Eye Tracking for Analyzing Abstract Paintings" 
where humans awarding scores found colors like yellow and green to be more positive than purples and reds. The artwork that was selected as more positive contained 
more white and lighter colors while the negative end of the spectrum consisted of darker colors. We are interested in the color histograms or color sets of paintings 
to contribute to our calculation of the artwork's sentiment. Our expected result is for paintings with lots of white, yellow, green, and light or bright colors 
to be associated with music of major keys that evoke more happy and light sentiments.
2. Number of colors: Another feature we are interested in, to determine how "chaotic" the painting is. If there is one dominant color, 
we will more likely pair the painting with music having one major melody or theme. If there are many colors represented, 
we will more likely choose music that does not have a dominant melodic line but many different instruments contributing to the music simultaneously.
3. Color contrast: We will also be analyzing the images using the HSV color model. Using this, we will determine the contrast between colors present. 
Low contrast makes for a more smooth, seamless image, and thus we will choose music that is slower and more fluid. 
Images with high contrast convey a more dramatic sentiment, and thus will be matched with faster and more dramatic music.
4. Color brightness: Using HSV and RGB, we will also be analyzing the darkness of the colors. Paintings that mostly feature light colors 
feel brighter and thus would align with musical instruments in higher registers, such as the piccolo or violin. 
Conversely, darker color schemes convey a more serious tone, better captured by lower register instruments such as the cello or bass.
5. Color saturation: Using HSV we will be looking at saturation of colors to capture the heaviness of colors present. 
Paintings where colors have higher saturation will feel heavier, and thus pair with music with richer textures 
including many and more varied instrumentation. Lower saturation would conversely match to music is minimal texture, 
like a solo with simple accompaniment. This is a stretch goal as we are already incorporating several, very different visual features.

## Measurement of Results
The results will be measured in several ways. Initially, we will use personal judgment to determine accuracy of the art sentiment tagging. 
Using the features defined in the previous section, we will see if the algorithm can provide a well matched tag and experience the art with corresponding music. 

Once we have a basic functioning prototype, we plan on getting the first round of feedback in two ways: in person and online. 

For both, we will restrict the study to five abstract art pieces and top two music matching for each. 
For most clear data, we will be focusing on selecting art pieces that emphasize the color and number of color features as we expect these to be most strong factors.

For the in person study group aspect of the feedback, we will gather at least ten students, aiming for a varied set of art background. The online survey will be posted on both social media 
and open forums for wider audience reach. Both will follow the following procedure:
1. Fill out general information and background in art and music: name, age, gender, interaction with art (0-4), attachment to art (0-4), interaction with music, attachment to music (0-4).
2. Show student one of three images, first with no music. Ask student to observe image for 30s-1min and then note whether image evokes any feeling or thought. Scale of 0-4 used with room for qualitative comment.
3. Add best matched music to art piece according to algorithm and listen to 30s-1min. Note additional changes in feeling or thought evoked by music. Scale of 0 to 4 to note degree of change with room for qualitative comment.
4. Give student option to try other music matching with piece. Repeat feedback collection as in step 3.
5. Allow user to repeat whole process with one of the other art pieces.
6. At end of experience, ask for scale 0-4 of experience and qualitative thoughts on art and music.

After receiving feedback, we will see review the feedback and note which features seemed more successful at evoking additional sentiment to art. We will then implement changes to weighting of the algorithm and have another round user feedback with broader art and music selection. Both will be coded into web app for full experience before final round of feedback.

## Related Journals and References}
### Journals and Technical Articles}
1. "In the Eye of the Beholder: Employing Statistical Analysis and Eye Tracking for Analyzing Abstract Paintings": https://staff.fnwi.uva.nl/e.bruni/publications/yanulevskaya-etal-acm-2012.pdf

    In this paper, Yanulevskaya and Uijlings et al. explore the question of whether a machine can be trained to understand the same emotional messages 
    in abstract art that human viewers can. In their analysis of 500 abstract paintings scored negative to positive on a Likert scale of 1 to 7, 
    they built a recognition system that associated statistical patterns with positive and negative emotions. They went further 
    to identify which portions of the abstract artworks correlated with which emotions. In their study, they also collected data of human participants 
    of varying ages and knowledge about art judging the emotion (positive to negative) of abstract art and include a graphic in their paper of the pieces.
    They noticed that darker colors indicate negative emotion and bright colors are associated with positive emotion. 
    They also found that smooth lines also evoke positive emotion and "chaotic texture" shows negative sentiment.
2. "Emotional Responses to Art: From Collation and Arousal to Cognition and Emotion": https://www.researchgate.net/publication/232468613_Emotional_Responses_to_Art_From_Collation_and_Arousal_to_Cognition_and_Emotion

    Silvia explores the history of art sentiment analysis, beginning with Berlyne's psychobiological model to new appraisal theories of emotions 
    in relation emotional response prediction to art. Berlyne's model focused around "collative variables", which are complexity, novelty, uncertainty,
    and conflict in art, and arousal to these features as reward response to art. These features were studied over varying types of art 
    including randomly generated shapes, melodies, visual art, with cross-cultural participants of varying art training level, and measuring broad range 
    of rating styles such as time spent viewing, choices between objects, quantitative scoring. These studies showed the collative arousal-inducing features 
    correlated more to interest than positive emotion. Thus the paper explores modern analysis using appraisal theories of emotion for art, as opposed to 
    Berlyne's arousal theories. Appraisal theories allow for differentiation of emotions that were evoked, as opposed to just any emotion being aroused in a participant. 
    Silvia explores and contrasts results of studies done around appraisal-based emotion and emphasizes the necessity to distinguish different emotions in art sentiment analysis.
3. "Sentiment Analysis in the Planet Art: a Case Study in the Social Semantic Web": http://www.di.unito.it/~argo/papers/RT0112.pdf

    In their work Baldoni et al. extract sentiment from tags of digitized visual artworks and evaluate this system, ArsEmotica, 
    through a user study involving the same users who tagged the artworks. The basic emotions used were the following: 
    sadness, happiness, surprise, fear, and anger. We will use their work to inform our sentiment categories. Another interesting takeaway 
    from their study is that often different users attached different sentiments to the same piece of artwork, indicating that emotional response 
    to art can be very individual.
4. "Measuring Music-Induced Emotion: A Comparison of Emotion Models, Personality Biases, and Intensity of Experiences": https://journals.sagepub.com/doi/10.1177/102986491101500203

    In this paper, Vuoskoski and Eerola explores music-specific and general emotion models to assess music-induced emotions. The paper studies 148 participants 
    who listened to 16 film music excepts and rated emotions evoked across different emotion models. From this, the researchers conclude that to minimize effect of personal factors 
    like mood or personality on emotion evoked, one must take care to use appropriate emotion models, namely the dimensional -- and also the simplest -- model. 
5. "Visual Sentiment Analysis for Social Images Using Transfer Learning Approach": https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7723683

    Researchers Islam and Zhang discuss their work devising a deep convolutional neural network to classify the sentiment of images. 
    They motivate their work by identifying visual content as an increasing body of data on the internet and on social networking sites 
    that people use to convey emotions. Using a CNN model required large-scale training data and supervised learning to be effective. 
    This means that not only is a large amount of data necessary, but also this data must be labeled. To circumvent these issues, 
    the researchers used transfer learning and hyper-parameters for CNN initialization and were able to improve performance. 
    In our project, we attempt to build a visual sentiment analyzer with more simplicity and clarity than a very deep neural network 
    by using features like color brightness, saturation, density, and contrast. We think we may be able to achieve relatively high accuracy 
    with a more simple and intuitive sentiment analysis algorithm.

### Technology and Database References
1. OpenCV-python: Our main tech stack for the algorithm will be the OpenCV API for image loading and relevant analysis. We plan on using the python library 
as it contains necessary tools for our preliminary features. 
[https://docs.opencv.org/master/d6/d00/tutorial_py_root.html, 
https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/, 
https://realpython.com/python-opencv-color-spaces/]
2. WikiArt Database: This will be our main database for art imagery as it comes cleaned, sorted, and indexed 
by type and artist. As explained above we will select several artists, totalling ~1000 abstract pieces, 
to do our sentiment tagging and music matching for. 
[https://www.wikiart.org/en/paintings-by-style/abstract-art#!#filterName:all-works,viewType:masonry]
3. Spotify Web API: This will be our external API for music matching based on sentiment, which is built into each song accessible by the Spotify API. 
[https://developer.spotify.com/documentation/web-api/]
