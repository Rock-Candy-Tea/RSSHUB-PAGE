
---
title: '原声js模拟直播弹幕滚动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9806afbc9d2429fb52e6688080e2eae~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 19:06:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9806afbc9d2429fb52e6688080e2eae~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、基本原理</h3>
<p>首先将直播区域分成十份（我个人自己为了便于计算分成十份），将输入的内容随机放到分成的十份区域中，插入到十份区域右边的视图之外，然后调用动画，按照随机的速度从右向左移动，当移动到左侧区域视图之外移除此滚动元素。</p>
<h3 data-id="heading-1">2、具体代码</h3>
<pre><code class="copyable"><div class="move_video_content">
    <div class="video_content">
        <div class="video_div" id="video_view"></div>
        <div class="scroll_content">
            <ul class="scroll_ul" id="scroll_ul_id"></ul> 
        </div>
    </div>
    <div class="input_content">
            <input type="text" class="input_text" maxlength="30" placeholder="请输入要发送的弹幕" id="input_text_id">
            <button type="button" class="button_btn" id="send_btn">发送</button>
    </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9806afbc9d2429fb52e6688080e2eae~tplv-k3u1fbpfcp-watermark.image" alt="1626144330(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">js代码如下</h4>
<pre><code class="copyable">let inputText = document.getElementById("input_text_id");//input输入框
let scrollContent = document.getElementById("scroll_ul_id");//侧边聊天栏
let videoView = document.getElementById("video_view");//视频区域
let videoWidth = videoView.offsetWidth;//直播区域的总宽度
let listHeight = videoView.offsetHeight/10;//每一层直播区域的高度
let listTopNum = [0,1,2,3,4,5,6,7,8,9];//将直播区域的高度分成10层
document.getElementById("send_btn").addEventListener("click",function()&#123;//监听发送按钮
    let value = inputText.value;//获取输入框的值
    if(!value) return;
    appendDom(value);//将输入框的值插入到滚动聊天中
    createVideoBulletChatDom(value);//将输入框的值插入到弹幕中
    inputText.value = '';//清空输入框
    scrollContent.scrollTop = scrollContent.scrollHeight;//自动滚动到底部
&#125;)
function appendDom(value)&#123;//将输入框的值插入到滚动聊天中
    let li = document.createElement("li");
    li.setAttribute("class","scroll_li");
    li.innerHTML = value;
    scrollContent.appendChild(li);
&#125;
let speedArr = ['normal','fast','faster'];
function createVideoBulletChatDom(value)&#123;//将输入框的值插入到弹幕中
    let num = listTopNum[Math.floor((Math.random()*listTopNum.length))];
    let p = document.createElement("p");
    p.setAttribute("class","video_p");
    p.style.top = (num * 60) + "px";
    p.style.left = videoWidth + "px";
    p.innerHTML = value;
    videoView.appendChild(p);
    let speed = speedArr[Math.floor((Math.random()*speedArr.length))];
    Animate(p,speed);//滚动动画
&#125;
let animateType = &#123;
    'normal':5,
    'fast':10,
    'faster':15
&#125;
function Animate(dom,speed)&#123;//滚动动画
    let domWidth = dom.offsetWidth;//当前弹幕元素的宽度
    let distance = videoWidth;//直播区域的总宽度
    speed ? speed : 'normal';
    let interval = animateType[speed]
    let timer = setInterval(function()&#123;
            distance -= interval;
            dom.style.left = distance + 'px';
            if(distance <= -domWidth)&#123;
                clearInterval(timer);
                videoView.removeChild(dom);//清除已经滚动出屏幕的标签
            &#125;
    &#125;,50)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据直播区域分成的十份（listTopNum），获取每一层区域的高度（listHeight），然后改变滚动标签的top实现插入到十份中的不同区域。
创建一个滚动标签就创建一个滚动动画（函数Animate），默认速度是normal，每次创建动画都会随机传入一个随机速度类型（normal、fast、faster），按照传入的速度类型来改变每次滚动减去的距离大小，实现不同的滚动速度。</p>
<h3 data-id="heading-3">总结</h3>
<p>这是个人闲着无事一时兴起写的一个直播滚动动画，<strong>如果加上WebSocket就能实现多人同步通信，这个以后无事再做完善。</strong>
具体代码请访问[：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fliqc-wwl%2Fbullet-chat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/liqc-wwl/bullet-chat" ref="nofollow noopener noreferrer">github.com/liqc-wwl/bu…</a>]
下载下来就能直接看效果。</p></div>  
</div>
            