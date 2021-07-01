
---
title: '纯js实现"罗盘"时钟'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/685fcbb9e6c4487386e35e7a6fdbded3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:42:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/685fcbb9e6c4487386e35e7a6fdbded3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/685fcbb9e6c4487386e35e7a6fdbded3~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-06-30_17-06-56.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">纯js实现"罗盘"时钟</h1>
<p>步骤一：首先需要将多个文字元素呈圆形排放；
步骤二：按一定角度进行旋转。</p>
<h2 data-id="heading-1">创建外围框架</h2>
<pre><code class="copyable">`<div class="home">
    <!--年-->
    <div class="year"></div>
    <!--月-->
    <div class="wrapper">
        <div class="circle month"></div>
    </div>
    <!--日-->
    <div class="wrapper">
        <div class="circle days"></div>
    </div>
    <!--时-->
    <div class="wrapper">
        <div class="circle hours"></div>
    </div>
    <!--分-->
    <div class="wrapper">
        <div class="circle minutes"></div>
    </div>
    <!--秒-->
    <div class="wrapper">
        <div class="circle seconds"></div>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>

<pre><code class="copyable">.home &#123;
    width: 100%;
    height: 100%;
    min-height: 660px;
    min-width: 800px;
    background-color: #000000;
    position: relative;
    color: #666666;
    padding: 20px 0;
    overflow: hidden;
&#125;

.wrapper, .year &#123;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
&#125;

.circle &#123;
    position: relative;
    /*// 添加动画效果*/
    transition: transform 0.4s ease-in-out;
&#125;

.circle span &#123;
    position: absolute;
    white-space: nowrap;
    font-size: 14px;
&#125;

/*// 激活时文字颜色为白色*/
.circle span.active &#123;
    color: #f60;
    font-weight: 700;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">实现外围秒</h2>
<p>根据不同的元素(月、日、时、分、秒)设置外围盒子的宽高，即设置circle盒子的大小，通过函数获取节点，并设置宽高</p>
<pre><code class="copyable">let boxSize = &#123;
        seconds: 580,
        minutes: 440,
        hours: 320,
        days: 180,
        month: 80
&#125;,
// 设置父盒子大小
function divStyle(node, key, deg) &#123;
    node.style.width = data.boxSize[key] + 'px';
    node.style.height = data.boxSize[key] + 'px';
    node.style.transform = `rotate(-$&#123;deg&#125;deg)`
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建子节点span，有多少个元素，则创建多少个span标签，将其append到div盒子中</p>
<pre><code class="copyable">function createSpanNode(texts, node, nodeSize, childNode) &#123;
    //texts对应当前的元素，node为父节点对象， nodeSize为父盒子大小
    //创建碎片节点
    let fragment = document.createDocumentFragment();
    for (let i = 0; i < texts.length; i++) &#123;
        //创建span节点
        let spanNode = document.createElement('span');
        spanNode.innerText = texts[i];
        //添加公共class
        spanNode.className = childNode;
        //添加样式
        spanStyle(spanNode, nodeSize, texts, i);
        //添加节点
        fragment.appendChild(spanNode);
    &#125;
    //添加节点
    node.appendChild(fragment);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置span盒子对应的旋转角度、样式等</p>
<pre><code class="copyable">// span盒子样式
function spanStyle(node, size, texts, index) &#123;
    // node：节点，size：盒子大小，texts：盒子渲染数据，index：对应span个数
    const r = size / 2; //半径
    const deg = getPerDeg(texts); //元素平均间隔度数
    const angle = deg * index;//夹角
    const &#123;a, b&#125; = getHypotenuse(r, angle);
    node.style.top = a + r + 'px';
    node.style.left = b + r + 'px';
    node.style.transform = `rotate($&#123;angle&#125;deg)`;
    node.style.transformOrigin = '0 0';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>抽离的公共方法</p>
<pre><code class="copyable">// 元素平均间隔度数
function getPerDeg(texts) &#123;
    return 360 / texts.length;
&#125;

// 已知角度和斜边，获取直角边
function getHypotenuse(long, angle) &#123;
    // 获得弧度
    let radian = 2 * Math.PI / 360 * angle;
    return &#123;
        a: Math.sin(radian) * long, // 邻边
        b: Math.cos(radian) * long // 对边
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>间隔一秒调用runClock方法</p>
<pre><code class="copyable">// 间隔1秒运行
let currentSeconds = 0, secondsDeg = 0;
let secondsTexts = ['零零',......,'五十九秒'];
function runClock() &#123;
    const d = new Date();
    const seconds = d.getSeconds(); // 秒
    currentSeconds = seconds;
    secondsDeg += getPerDeg(secondsTexts);
    divStyle(secondsNode, 'seconds', secondsDeg);
    spanDynamicStyle(secondsNode, currentSeconds);
&#125;
// 获取节点
function getDivNode(classname) &#123;
    return document.getElementsByClassName(classname)[0];
&#125;
// 设置class类(动态)
function spanDynamicStyle(node, currentIndex) &#123;
    if (currentIndex === 0 && node.childNodes[node.childNodes.length - 1].className.includes('active')) &#123;
        node.childNodes[node.childNodes.length - 1].classList.remove('active');
    &#125;
    if (currentIndex > 0 && node.childNodes[currentIndex - 1].className.includes('active')) &#123;
        node.childNodes[currentIndex - 1].classList.remove('active');
    &#125;
    node.childNodes[currentIndex].classList.add('active');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>月、日、时、分同理实现</p>
<h2 data-id="heading-3">实现年显示</h2>
<pre><code class="copyable">// 设置年
(function setYear() &#123;
    let num = &#123;0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'&#125;
    document.getElementsByClassName('year')[0].innerText = new Date().getFullYear().toString().split('').map(item => num[item]).join('')
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码地址<a href="https://github.com/L-Xiaobai/clock" target="_blank" rel="nofollow noopener noreferrer">：Github</a></p></div>  
</div>
            