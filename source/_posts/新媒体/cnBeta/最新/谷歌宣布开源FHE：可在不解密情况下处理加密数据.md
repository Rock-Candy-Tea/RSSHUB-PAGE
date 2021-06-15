
---
title: '谷歌宣布开源FHE：可在不解密情况下处理加密数据'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0615/cec7e8a910e813b.jpg'
author: cnBeta
comments: false
date: Tue, 15 Jun 2021 07:50:44 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0615/cec7e8a910e813b.jpg'
---

<div>   
在今天发布的官方博文中，Google宣布开源全同态加密（<a href="https://developers.googleblog.com/2021/06/our-latest-updates-on-fully-homomorphic-encryption.html" target="_blank">Fully Homomorphic Encryption</a>，简称 FHE）。目前相关源代码已经托管在 <a href="https://github.com/google/fully-homomorphic-encryption" target="_blank">GitHub </a>上了。这是Google首创的通用转码器，这将使开发人员无法访问个人身份信息的前提下，能够在加密数据上进行计算。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0615/cec7e8a910e813b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0615/cec7e8a910e813b.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0615/f2e55975afb2d4a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0615/f2e55975afb2d4a.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Google表示通过 FHE，加密的数据可以穿过互联网到达服务器，在那里可以在不被解密的情况下进行处理。Google的转码器将使开发人员能够为任何类型的基本计算编写代码，如简单的字符串或数字处理，并在加密数据上运行它。转码器将把这些代码转换成可以在加密数据上运行的版本。这样，开发人员就可以创建不需要未加密数据的新编程应用程序。FHE 也可用于以私人方式在敏感数据上训练机器学习模型。</p><p style="text-align: left;">例如，设想你正在为糖尿病患者建立一个应用程序。这个应用程序可能会收集用户的敏感信息，你需要一种方法来保持这些数据的隐私和保护，同时也与医学专家分享这些数据，以了解有价值的见解，从而实现重要的医学进步。通过Google为 FHE 提供的转接器，你可以对你收集的数据进行加密，并与医学专家分享，而医学专家又可以在不解密的情况下对数据进行分析--为医学界提供有用的信息，同时确保没有人可以获取数据的基本信息。</p>   
</div>
            