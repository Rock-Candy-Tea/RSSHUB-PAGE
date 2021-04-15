
---
title: 'Using AI to predict retinal disease progression'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=7148'
author: DeepMind
comments: false
date: Mon, 18 May 2020 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7148'
---

<div>   
<p><span style="font-weight: 400;">Vision loss among the elderly is a major healthcare issue: about one in three people have some vision-reducing disease by the age of 65. Age-related macular degeneration (AMD) is the most common cause of blindness in the developed world. In Europe, approximately </span><a href="https://www.ncbi.nlm.nih.gov/pubmed/31712255"><span style="font-weight: 400;">25% of those 60 and older</span></a><span style="font-weight: 400;"> have AMD. The ‘dry’ form is relatively common among people over 65, and usually causes only mild sight loss. However, about 15% of patients with dry AMD go on to develop a more serious form of the disease – exudative AMD, or exAMD – which can result in rapid and permanent loss of sight. Fortunately, there are treatments that can slow further vision loss. Although there are no preventative therapies available at present, these are being explored in clinical trials. The period before the development of exAMD may therefore represent a critical window to target for therapeutic innovations: can we predict which patients will progress to exAMD, and help prevent sight loss before it even occurs?</span></p>
<p><span style="font-weight: 400;">In our latest work, published in <a href="https://www.nature.com/articles/s41591-020-0867-7">Nature Medicine</a>, we </span><a href="https://deepmind.com/blog/article/predicting-eye-disease-moorfields"><span style="font-weight: 400;">collaborated with Moorfields Eye Hospital</span></a><span style="font-weight: 400;"> and </span><a href="https://health.google/"><span style="font-weight: 400;">Google Health</span></a><span style="font-weight: 400;"> to curate a dataset of images of eye retinas, train an artificial intelligence (AI) system that could predict the development of exAMD, and conduct a study to evaluate our model compared with expert clinicians. We demonstrate that our system is able to perform as well as, or better than, clinicians at predicting whether an eye will convert to exAMD in the next 6 months. Lastly, we explore the potential clinical applicability of our system. Our contribution highlights the potential of using AI in preventative studies for diseases such as exAMD.</span></p>
<h3><span style="font-weight: 400;">The Moorfields Eye Hospital AMD dataset</span></h3>
<p dir="ltr"><span style="font-weight: 400;">We used a dataset of anonymised retinal scans from Moorfields patients with exAMD in one eye, and at high-risk of developing exAMD in their other eye. This comprises 2,795 patients across seven different Moorfields sites in London, with representation across genders, age ranges, and ethnicities. These patients attend the hospital regularly to receive treatment, undergoing high-resolution three-dimensional optical coherence tomography (OCT) imaging of both eyes, at each visit. There is often a delay between when exAMD has developed and when it is diagnosed and treated. To address this, we worked with retinal experts to review all scans for each eye and specify the scan when exAMD was first evident.</span></p>
<h3><span style="font-weight: 400;">Training an early warning system for AMD</span></h3>
<p><span style="font-weight: 400;">Our system is composed of two deep convolutional neural networks that take as input high-dimensional volumetric eye scans, where each scan consists of 58 million three-dimensional pixels (voxels). In our </span><a href="https://deepmind.com/blog/article/moorfields-major-milestone"><span style="font-weight: 400;">previous work</span><span style="font-weight: 400;">, now continuing in collaboration with </span></a><span style="font-weight: 400;">Google Health, we developed a model capable of segmenting these eye scans into thirteen anatomical categories. The segmented data was combined with the raw scan and both were used as inputs to the prediction model, which was trained to estimate a patient’s risk of conversion to exAMD in their other eye within the next six months. </span></p>  
</div>
            