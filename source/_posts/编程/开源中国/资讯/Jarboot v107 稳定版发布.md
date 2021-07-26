
---
title: 'Jarboot v1.0.7 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8059'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 18:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8059'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></p> 
<p>重大特性更新：</p> 
<p>1、启动的jar文件配置支持<strong>绝对路径</strong>和<strong>相对路径</strong>两种方式；</p> 
<p>2、增加配置项：Jarboot启动后是否自动启动其管理的服务，默认不启动；</p> 
<p>3、原通用配置项的配置文件统一移到<strong>jarboot.properties</strong>配置文件中；</p> 
<p>4、启动的VM参数配置，配置项为为一个.vmoptions的配置文件，支持相对路径和绝对路径，多个服务可以共用一个vmoptions配置文件；</p> 
<p>5、工作路径和JDK的配置，支持相对路径和绝对路径；</p> 
<p>6、issue [#13] 命令行中引号内存在空格时解析错误的bug，修复完成；</p> 
<p>7、启动优先级排序错误bug的修复，优先级数值大者优先启动；</p> 
<p>8、VM参数和程序传入参数编辑支持弹窗富文本编辑；</p> 
<p>其他更新：</p> 
<p>1、消息推送机制重构，优化性能；</p> 
<p>2、增加startup和shutdown的脚本；</p> 
<p>3、移除swagger-ui；</p> 
<p>4、引入p3c等代码检查规范；</p> 
<p>5、Json序列化存在部分bug，fastjson -> jackson</p>
                                        </div>
                                      
</div>
            