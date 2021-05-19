
---
title: 'Jessibuca 2.0 发布，H5 直播流播放器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4883'
author: 开源中国
comments: false
date: Wed, 19 May 2021 09:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4883'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>2.0更新内容：</strong></p> 
<ul> 
 <li>同时支持H264和H265解码，无需重新加载解码器</li> 
 <li>音频支持AAC、PCMA、PCMU格式（也可以通过编译FFmpeg来支持更多格式）</li> 
 <li>代码大幅度精简，删去无用代码，C++代码减少了80%，网络通讯和协议解包部分移入js端实现，方便二次开发</li> 
 <li>实现OffscreenCanvas性能优化，CPU和内存消耗显著减少</li> 
 <li>音频解码实现了连续播放，解决了原来分段播放带来的瑕疵</li> 
 <li>采用最新的emscripten（2.0.20）和ffmpeg（4.4）版本编译，实现极限wasm压缩体积(1.2m)</li> 
 <li>clone项目后运行vuepress dev . （提前安装好vuepress，注意命令后面有个点）即可看到效果</li> 
</ul> 
<p style="text-align:left"><strong>软件介绍：</strong></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#2c3e50">Jessibuca是一款开源的纯H5直播流播放器，通过Emscripten将音视频解码库编译成Js（ams.js/wasm)运行于浏览器之中。兼容几乎所有浏览器，可以运行在PC、手机、微信中，无需额外安装插件。</span></p> 
<ul> 
 <li>支持解码H.264视频(Baseline, Main, High Profile全支持，支持解码B帧视频)</li> 
 <li>支持解码H.265视频（flv id == 12）</li> 
 <li>支持解码AAC音频(LC,HE,HEv2 Profile全支持)</li> 
 <li>支持解码PCMA音频以及PCMU音频格式</li> 
 <li>可设置播放缓冲区时长，可设置0缓冲极限低延迟（网络抖动会造成卡顿现象）</li> 
 <li>支持智能不花屏丢帧，长时间播放绝不累积延迟。</li> 
 <li>可创建多个播放实例</li> 
 <li>程序精简，经CDN加速，GZIP压缩（实际下载500k），加载速度更快</li> 
 <li>同时支持http-flv和websocket-flv协议以及websocket-raw私有协议（裸数据，传输量更小，需要搭配Monibuca服务器） 注：以http-flv请求时，存在跨域请求的问题，需要设置access-control-allow-origin, websocket-flv默认不存在此问题</li> 
 <li>支持HTTPS/WSS加密视频传输，保证视频内容传输安全</li> 
 <li>手机浏览器内打开视频不会变成全屏播放</li> 
</ul>
                                        </div>
                                      
</div>
            