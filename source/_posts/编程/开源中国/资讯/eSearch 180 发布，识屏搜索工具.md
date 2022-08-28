
---
title: 'eSearch 1.8.0 发布，识屏搜索工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=62'
author: 开源中国
comments: false
date: Sun, 28 Aug 2022 12:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=62'
---

<div>   
<div class="content">
                                                                                            <p>eSearch 1.8.0 已经发布，识屏搜索工具。</p> 
<h1>1.8.0</h1> 
<h2>主要更新</h2> 
<p>离线OCR额外文件、ffmpeg一起打包到安装包中，无需额外下载，开箱即用。原先额外下载的文件可以删除了。</p> 
<p>离线OCR使用paddleOCR v3模型，并使用onnxruntime-web推理。速度可能会降低一些，精度的变化感知不强，但带来一些好处：离线OCR开箱即用和方便多种模型管理。</p> 
<p>未来还可能会调用webgl，若是介意这个版本的性能，可不升级（此版本没有特别重大的更新），等待之后版本的性能优化:D</p> 
<p>欢迎大家为这个项目点亮star！</p> 
<h2>新增</h2> 
<ul> 
 <li>离线OCR 
  <ul> 
   <li>拖动模型文件添加模型</li> 
   <li>管理多个OCR模型（可以切换多种语言）</li> 
  </ul> </li> 
 <li>主要 
  <ul> 
   <li>点击托盘按钮直接自动搜索</li> 
   <li>托盘OCR和以图搜图快捷按钮</li> 
  </ul> </li> 
 <li>录屏 
  <ul> 
   <li>任务进度提示和输出</li> 
  </ul> </li> 
</ul> 
<h2>修复</h2> 
<ul> 
 <li>设置 
  <ul> 
   <li>无法显示版本</li> 
   <li>无法设置配置位置</li> 
   <li>文字反色错误</li> 
  </ul> </li> 
</ul> 
<h2>优化</h2> 
<ul> 
 <li>离线OCR 
  <ul> 
   <li>无需额外下载</li> 
  </ul> </li> 
 <li>录屏 
  <ul> 
   <li>无需额外下载ffmpeg</li> 
  </ul> </li> 
 <li>设置 
  <ul> 
   <li>使用蓝色主题色，深色模式下更醒目</li> 
  </ul> </li> 
</ul> 
<p><strong>全部更新日志</strong>: <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fxushengfeng%2FeSearch%2Fcompare%2F1.7.4...1.8.0" target="_blank">https://github.com/xushengfeng/eSearch/compare/1.7.4...1.8.0</a></p> 
<p>详情查看：<a href="https://gitee.com/xsf-root/eSearch/releases/1.8.0">https://gitee.com/xsf-root/eSearch/releases/1.8.0</a></p>
                                        </div>
                                      
</div>
            