
---
title: 'vue 中实现同时弹出多个div 并移动弹框位置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca06944fa1b2423f8e094f7a54a66b87~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 21:07:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca06944fa1b2423f8e094f7a54a66b87~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">需求</h1>
<p>同一界面多个设备，需要点击查看详情，且可以同时点开多个div详情框，进行详情数据对比查看。</p>
<h1 data-id="heading-1">效果</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca06944fa1b2423f8e094f7a54a66b87~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">思考</h1>
<p>最初考虑通过el-dialog实现，但是怎么尝试设置属性，都只能一层层弹出，切存在蒙版层难以设置div的层级关系，无法同时弹出多个对话框切换使用。</p>
<p>最后考虑通过v-for控制div的动态渲染来实现。</p>
<h1 data-id="heading-3">关键代码</h1>
<p>点击设备按钮和div动态渲染部分</p>
<pre><code class="copyable"><div class="just-click" @click="clickRect('101')" style="left:200px;top:300px;">101</div>
<div class="just-click" @click="clickRect('102')" style="left:400px;top:300px;">102</div>
<div class="just-click" @click="clickRect('103')" style="left:600px;top:300px;">103</div>
<!-- 动态渲染弹出框 -->
<div v-for="devOne in devDialogs" :key="devOne.devCode" class="multi-dialog" :id="devOne.box" :style="&#123;left: devOne.left, top: devOne.top&#125;">
  <div class="multi-dialog-title" :id="devOne.title">
    <span>&#123;&#123; devOne.devCode &#125;&#125;</span>
    <button type="button" aria-label="Close" class="el-dialog__headerbtn" @click="closeDialog(devOne)">
      <i class="el-dialog__close el-icon el-icon-close"></i>
    </button>
  </div>
  <div class="multi-dialog-content">
    <!-- <bpg-kzmb></bpg-kzmb> -->
    假设此处有内容
  </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式设置部分</p>
<pre><code class="copyable">.just-click &#123;
  cursor: pointer;
  width: 100px;
  height: 40px;
  position: fixed;
  background: white;
  color: black;
  line-height: 40px;
  text-align: center;
&#125;
.multi-dialog &#123;
  position: fixed;
  width: 580px;
  background: rgba(0,93,172,0.75);
  box-shadow: 0px 0px 12px rgba(0,186,255,0.5);
  top: 20px;
  left: 20px;
  z-index: 10;
  font-size: 14px;
&#125;
.multi-dialog-title &#123;
  padding: 20px;
  border: 1px solid rgba(0,93,172,0.75);
  border-top: 2px solid rgba(127,255,255);
  cursor: move;
  font-size: 18px;
&#125;
.multi-dialog-content &#123;
  padding: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>js动态控制部分</p>
<pre><code class="copyable">data () &#123;
    return &#123;
    devDialogs: []
    &#125;
&#125;
// 点击设备按钮弹出弹框
clickRect (val) &#123;
  // 动态展示设备弹框
  let exist = false
  this.devDialogs.forEach(element => &#123;
    if (val === element.devCode) &#123;
      exist = true
    &#125;
  &#125;)
  if (!exist) &#123;
    let devOne = &#123;
      devCode: val,
      box: 'box' + val,
      title: 'title' + val,
      left: '20px',
      top: '20px'
    &#125;
    this.devDialogs.push(devOne)
    this.$nextTick(() => &#123;
      this.divMove(devOne.title, devOne.box)
    &#125;)
  &#125;
&#125;,
// 关闭设备弹框
closeDialog (devOne) &#123;
  this.devDialogs.forEach(function (item, index, arr) &#123;
    if (item.devCode === devOne.devCode) &#123;
      arr.splice(index, 1)
    &#125;
  &#125;)
&#125;,
// 移动设备弹框
divMove (titleId, boxId) &#123;
  let title = document.getElementById(titleId) // 获取点击元素（可选中拖动的部分）
  let box = document.getElementById(boxId) // 获取盒子元素（需要移动的整体）
  let divX = 0 // div的x坐标
  let divY = 0 // div的y坐标
  let isDrop = false // 是否可拖动 按下鼠标置为true 松开鼠标置为false
  let self = this
  // 将鼠标点击事件绑定在顶部title元素上
  title.onmousedown = function (e) &#123;
    let el = e || window.event // 获取鼠标位置
    divX = el.clientX - box.offsetLeft // 鼠标相对盒子内部的坐标x
    divY = el.clientY - box.offsetTop // 鼠标相对盒子顶部的坐标y
    isDrop = true // 设为true表示可以移动
    document.onmousemove = function (e) &#123;
      // 是否为可移动状态
      if (isDrop) &#123;
        let el = e || window.event
        let leftX = el.clientX - divX // 盒子距窗口左边的距离
        let leftY = el.clientY - divY // 盒子距窗口顶部的距离
        // 盒子不超出窗口的最大移动位置 即拖动置右下角时
        let maxX = document.documentElement.clientWidth - box.offsetWidth // 窗口宽度-盒子宽度
        let maxY = document.documentElement.clientHeight - box.offsetHeight // 窗口高度-盒子高度
        // 当移动到最左最上时，leftX < 0、leftY < 0，盒子左边距、上边距取最大值0
        // 当移动到最右最下时，leftX > maxX、leftY > maxY、已超出边界，盒子左边距、上边距取maxX、maxY
        leftX = Math.min(maxX, Math.max(0, leftX))
        leftY = Math.min(maxY, Math.max(0, leftY))
        box.style.left = leftX + 'px'
        box.style.top = leftY + 'px'
      &#125;
    &#125;
    document.onmouseup = function () &#123;
      // 防止删除上一个div，下一个div挪位到上一个，需要在停止移动时给div赋位置
      self.devDialogs.forEach(function (item) &#123;
        if (item.box === boxId) &#123;
          item.left = box.style.left
          item.top = box.style.top
        &#125;
      &#125;)
      isDrop = false
      document.onmousemove = null
      document.onmouseup = null
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">注意点</h1>
<h2 data-id="heading-5">1、onmousemove和onmouseup的位置</h2>
<p>如果把onmousemove和onmouseup写在onmousedown的外面，会导致后面的div覆盖前面的，isDrop仅仅是最后一个弹框的isDrop标识。</p>
<h2 data-id="heading-6">2、z-index处理</h2>
<p>其实不用额外对z-index进行处理就解决了需求，最开始很烦这个z-index咋控制啊很麻烦啊，结果不控制也可以。</p>
<h2 data-id="heading-7">3、.multi-dialog样式设置</h2>
<p>.multi-dialog设置position为absolute会局限在上一层底下移动，若要跳出局限到整个窗口，只需设置position: fixed;即可。</p>
<h2 data-id="heading-8">4、动态渲染div时的key的正确绑定很重要！！！</h2>
<p><strong>有问题的绑定方式：</strong></p>
<pre><code class="copyable"><div v-for="(devOne, index) in devDialogs" :key="index" class="multi-dialog" :id="devOne.box" :style="&#123;left: devOne.left, top: devOne.top&#125;">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>乍一看似乎功能都很正常，通过数组的index来绑定key确实是唯一的，也不会有报错提示。</p>
<p>但是！！因为我们对devDialogs这个数组进行了增删操作，vue的渲染是根据index来的。</p>
<p>这样导致一个现象：</p>
<p>依次点击101、102，关闭101的弹框，再点击101，再移动102发现101会跟着移动，原因是移动102获取到的id竟然是101的，然后两弹框同时进行了移动，问题在于vue.js根据这个：key=index绑定的div，而我们对devDialogs数组进行增删操作时改动了对应div的index……讲不清了，因为我也不知道为什么，只知道就是这个原因，改成如下绑定key值即可。</p>
<p><strong>正确的绑定方式：</strong></p>
<pre><code class="copyable"><div v-for="devOne in devDialogs" :key="devOne.devCode" class="multi-dialog" :id="devOne.box" :style="&#123;left: devOne.left, top: devOne.top&#125;">
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结论：</strong>
严格根据div的唯一标识绑定key真的很重要！！！</p></div>  
</div>
            