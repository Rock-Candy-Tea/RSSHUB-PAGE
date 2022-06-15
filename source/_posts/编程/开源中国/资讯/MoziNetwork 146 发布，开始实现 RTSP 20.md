
---
title: 'Mozi.Network 1.4.6 发布，开始实现 RTSP 2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2100'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 14:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2100'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <div> 
   <div> 
    <p>Mozi.Network 是基于.Net 开发的<span>网络应用协议基础组件。包含 HTTP 服务器，IoT 服务端和客户端项目等网络通讯协议。</span></p> 
    <p>新增了一个HttpClient项目，用于对HTTP资源进行调试。</p> 
    <p><span>关于RTSP项目的进展，这一开发周期对RTSP所有的报文进行了分解，并开始实现RTSP,RTP,RTCP报文解析和构造。</span></p> 
    <p>同时新版本中有如下更新：</p> 
    <ol> 
     <li>增加HttpServer,HttpClient数据统计字段</li> 
     <li>增加HttpServer,HttpClient事件</li> 
     <li>修正HttpRequest->GetRequestLine的BUG</li> 
     <li>改HttpRequest->SetHeader为AddHeader</li> 
     <li>增加HttpClient中Content-Encoding的实现，并加入两种压缩算法</li> 
     <li>增加HttpClient的多路径请求方法</li> 
     <li>抽取HttpServer->HandleError,HandleNotFound方法</li> 
     <li>去掉Common/Log.cs中的记录文件名的日期要素</li> 
    </ol> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            