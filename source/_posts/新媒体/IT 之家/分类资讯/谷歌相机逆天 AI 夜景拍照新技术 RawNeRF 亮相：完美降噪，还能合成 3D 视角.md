
---
title: '谷歌相机逆天 AI 夜景拍照新技术 RawNeRF 亮相：完美降噪，还能合成 3D 视角'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://wx4.sinaimg.cn/orj480/002pQNxngy1h5gogrv42sj61hc0u0gqq02.jpg'
author: IT 之家
comments: false
date: Tue, 23 Aug 2022 14:50:46 GMT
thumbnail: 'https://wx4.sinaimg.cn/orj480/002pQNxngy1h5gogrv42sj61hc0u0gqq02.jpg'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1649408" rel="nofollow">蓝色海岸</a> 的线索投递！</div>
            <p data-vmark="5eac"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 8 月 23 日消息，近日，国内网上有一段谷歌 AI 夜景拍照新技术 <span class="accentTextColor">RawNeRF </span>的视频火了，可以将夜晚照片完美降噪，精准还原，并且能将若干张 2D 照片合成 3D 视觉，并可调整焦点。</p><p data-vmark="c3bf" style="text-align: center;"><a class="ithome_super_player" contenteditable="false" target="_blank" data-timestamp="1661266587832" data-vpreview-url="https://f.video.weibocdn.com/u0/94V94cqGgx07YDH6YDlm01041201Kw3o0E010.mp4?label=mp4_720p&template=1280x720.25.0&ori=0&ps=1CwnkDw1GXwCQx&Expires=1661270131&ssig=4P%2F4qo9nnC&KID=unistore,video" href="https://weibo.com/2214257545/M2mADlCkV?refer_flag=1001030103_"><img src="https://wx4.sinaimg.cn/orj480/002pQNxngy1h5gogrv42sj61hc0u0gqq02.jpg" class="lazy" title="谷歌相机逆天 AI 夜景拍照新技术 RawNeRF 亮相：完美降噪，还能合成 3D 视角" referrerpolicy="no-referrer"></a></p><p data-vmark="06a7">IT之家发现，该技术的论文于 2021 年 11 月发表，也在 Github.io 上有主页，名为《NeRF in the Dark: High Dynamic Range View Synthesis from Noisy Raw Images》。</p><p data-vmark="f2a4" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/8/1dd285fc-0b61-4a4e-a4a8-f816a3c8c636.png" w="1349" h="845" title="谷歌相机逆天 AI 夜景拍照新技术 RawNeRF 亮相：完美降噪，还能合成 3D 视角" width="1349" height="514" referrerpolicy="no-referrer"></p><p data-vmark="7cc2">顾名思义，该技术可以通过 NeRF （神经辐射场）处理高噪点的夜间拍摄图像，从而将<span class="accentTextColor">充满噪点的 Raw 图像</span>合成高动态范围视图。</p><p data-vmark="088c" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/8/5e40da44-f213-43ab-8cba-e816f57e3bf6.png" w="998" h="870" title="谷歌相机逆天 AI 夜景拍照新技术 RawNeRF 亮相：完美降噪，还能合成 3D 视角" width="998" height="715" referrerpolicy="no-referrer"></p><p data-vmark="da62">NeRF 是一个简单的全连接神经网络，使用 2D 图像的信息作为训练数据，还原拥有体积的 3D 场景。</p><p data-vmark="3f94">原版 NeRF 使用色调映射的低动态范围 LDR 图像作为输入，而谷歌将 NeRF 修改为直接在线性原始图像上进行训练，<span class="accentTextColor">保留场景的完整动态范围</span>，可以有效地将 RawNeRF 变成一个多图像降噪器，能够组合来自数十或数百个输入图像的信息。</p><p data-vmark="cec5" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/8/9e0132f7-5b56-4daf-b0a1-6b1fa453c09a.png" w="904" h="680" title="谷歌相机逆天 AI 夜景拍照新技术 RawNeRF 亮相：完美降噪，还能合成 3D 视角" width="904" height="617" referrerpolicy="no-referrer"></p><p data-vmark="bb2e">除了改变相机视角之外，<span class="accentTextColor">RawNeRF 可以在后期调整焦点、曝光和色调映射</span>，也就是像视频中演示的那样。</p><p data-vmark="ea0c">IT之家小伙伴们应该都被谷歌相机的强大“夜视”功能惊艳过，如果 RawNeRF 能够用于谷歌相机，那么或许手机也能拍到清晰的夜间 3D 视觉图像，当然目前还没有。</p><p data-vmark="e0b3" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/8/c8e51843-6964-4278-865f-22830b50d217.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE1Ny5wbmc=,g_5,x_0,y_0,a_0,t_100" w="420" h="823" title="谷歌相机逆天 AI 夜景拍照新技术 RawNeRF 亮相：完美降噪，还能合成 3D 视角" width="420" height="823" referrerpolicy="no-referrer"></p><p data-vmark="7764" style="text-align: justify;"><strong>论文：</strong><span class="link-text-start-with-http">https://arxiv.org/abs/2111.13679</span></p><p data-vmark="f0d4" style="text-align: justify;"><strong>RawNeRF 介绍主页：</strong><span class="link-text-start-with-http">https://bmild.github.io/rawnerf/</span></p>
          
</div>
            