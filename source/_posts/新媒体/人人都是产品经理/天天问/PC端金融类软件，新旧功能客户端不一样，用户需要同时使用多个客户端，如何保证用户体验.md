
---
title: 'PC端金融类软件，新旧功能客户端不一样，用户需要同时使用多个客户端，如何保证用户体验'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 天天问
headimg: 'https://static.woshipm.com/YY_C_20220418_1650262798321031399.png'
author: 人人都是产品经理
comments: false
date: Wed, 20 Apr 2022 00:43:37 GMT
thumbnail: 'https://static.woshipm.com/YY_C_20220418_1650262798321031399.png'
---

<div>   
<p>PC端金融类软件，新旧功能客户端不一样，用户需要同时使用多个客户端，如何保证用户体验？</p><p><br></p><p>我们公司的金融客户端，有几百个标签页。新的功能使用electron网页端做的，旧的功能使用swing做的。这两个技术栈会产生两个客户端，用户使用时，需要在两个客户端中来回切换。如何保证用户没有割裂感，并提高用户体验。</p><p><br></p><p>每个客户端中都有一套 菜单，标签页体系。</p><p><br></p><p>swing客户端类似这样：</p><p><img src="https://static.woshipm.com/YY_C_20220418_1650262798321031399.png" title="TTW_QUESTION_202204_20220418141707_0694.png" alt="QQ截图20220418140318.png" referrerpolicy="no-referrer"></p><p>electron客户端类似这种：</p><p><img src="https://static.woshipm.com/YY_C_20220418_1650262798570086292.png" title="TTW_QUESTION_202204_20220418141713_0225.png" alt="QQ截图20220418140934.png" referrerpolicy="no-referrer"></p><p>我们现在的模式是，从swing端点击菜单时，弹出一个electron客户端，然后electron客户端中打开对应菜单。这样体验不好，需要来回切换。</p><p><br></p><p>请问有什么比较好的融合方式？</p>  
</div>
            