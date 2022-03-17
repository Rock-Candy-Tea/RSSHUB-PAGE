
---
title: 'msg.js 轻量级信息提示，一行代码调用，v1.6 升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0613/170427_f850a662_429922.png'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 14:18:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0613/170427_f850a662_429922.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0613/170427_f850a662_429922.png" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">更新说明</h1> 
<ol> 
 <li>优化多个弹出层共存时异常的问题</li> 
 <li>增加弹出层返回<span>id</span>，可用<span> msg.close</span>(<span>id</span>)<span> </span>来关闭指定的弹出层。</li> 
 <li>优化<span> msg.close </span>如果不传入<span>id</span>，每次点击默认关闭当前所存在的、最后一次的弹出层。</li> 
 <li><span>增加</span> msg.input <span>弹出单行输入框</span></li> 
 <li><span>增加</span> msg.textarea <span>弹出多行输入框</span></li> 
 <li>优化<span> msg.popup </span>有情况会显示不全的问题</li> 
 <li>优化被外部样式影响的问题</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">DEMO示例快速体验:</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fres.zvo.cn%2Fmsg%2Fdemo.html" target="_blank">https://res.zvo.cn/msg/demo.html</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">快速使用</h1> 
<h4 style="margin-left:0; margin-right:0; text-align:left">第一步，引入js</h4> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#55cde3"><span style="color:#333333"><</span><span style="color:#008080"><span style="color:#333333"><span style="color:#22863a">script</span></span></span><span style="color:#333333"> <span style="color:#6f42c1">src</span>=</span><span style="color:#dd1144"><span style="color:#333333"><span style="color:#032f62">"https://res.zvo.cn/msg/msg.js"</span></span></span><span style="color:#333333">></span></span><span style="color:#55cde3"><span style="color:#333333"></</span><span style="color:#008080"><span style="color:#333333"><span style="color:#22863a">script</span></span></span><span style="color:#333333">></span></span>
</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:start">第二步，实现代码，如</h4> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#d73a49">msg</span><span style="color:#6f42c1">.info</span>(<span style="color:#dd1144"><span style="color:#032f62">'哈喽'</span></span>);</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更多使用说明，参考:</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/leimingyun/dashboard/wikis/leimingyun/msgjs/preview?doc_id=1473987&sort_id=4111581">https://gitee.com/leimingyun/dashboard/wikis/leimingyun/msgjs/preview?doc_id=1473987&sort_id=4111581</a></p>
                                        </div>
                                      
</div>
            