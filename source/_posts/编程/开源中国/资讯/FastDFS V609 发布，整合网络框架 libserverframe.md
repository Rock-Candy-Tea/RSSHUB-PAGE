
---
title: 'FastDFS V6.09 发布，整合网络框架 libserverframe'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5758'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 10:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5758'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span><span>  </span>FastDFS V6.09</span>发布，主要改进：引入网络框架库<span>libserverframe</span>，替换原有的<span>tracker nio</span>和<span>storage nio</span>两个模块。<span> 2015</span>年<span>libserverframe</span>从<span>FastDFS</span>的<span>nio</span>模块抽取出来，现在<span>FastDFS</span>使用<span>libserverframe</span>，使得代码更加简洁高效，并解决了由来已久的一个<span>bug</span>：网络线程接收到客户端请求，把文件读写交给磁盘<span>IO</span>线程后，在磁盘线程处理过程中如果客户端断开连接，对应的网络线程将空转导致<span>CPU</span>跑满。解决方法是<span>task</span>对象使用引用计数器，网络线程和磁盘线程分别持有<span>task</span>对象（引用计数加一），各自处理完成后释放该<span>task</span>对象（引用计数减一），当引用计数为零时，才能将该<span>task</span>放回对象池。</p> 
<p><span>  </span>V6.09<span>另外两点改进：</span></p> 
<p><span><span>    </span>1</span>）<span>tracker server</span>和<span>storage server</span>均支持<span>-N</span>选项，表示程序在前台运行，而不采用传统的<span>daemon</span>运行方式，以方便和其他运维工具整合；</p> 
<p><span><span>    </span>2</span>）文件上传次数、文件下载次数等计数器不再采用线程锁，而是使用原子操作，这样代码更加简洁且性能更高。</p> 
<p><span>   </span>FastDFS V6.09 <span>依赖</span>libfastcommon<span>和</span>libserverframe<span>这两个基础库，欢迎大家下载使用，建议已有用户尽快升级到最新版本。</span></p>
                                        </div>
                                      
</div>
            