
---
title: 'Vue全局自定义指令实践-Modal拖拽'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fa8fffb02e5463d843cfae782d9b83b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 22:52:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fa8fffb02e5463d843cfae782d9b83b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>微信公众号：  <strong>[大前端驿站]</strong><br>
关注大前端驿站。问题或建议，欢迎公众号留言。</p>
</blockquote>
<p><strong>这是我参与8月更文挑战的第31天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">背景</h3>
<p>最近一直在做的项目是Vue2搭建的项目，UI框架用的antdV，项目中用到了很多Modal对话框，然后突然有一天产品说：“这个对话框为什么不能移动啊，挡住我看信息了”，那没办法，有需求就得做，这就是新生代打工人。</p>
<p>首先我去antdV官网看Modal的配置属性和方法，看看有没有这方面的属性或者方法可以直接解决，无奈没有找到。第二步开始问百度，相关的博客也有一些，但是总的来说五花八门，不是特别好搞懂，然后发现有个使用全局自定义指定的方式好像有点意思，然后开始自己的实操解决需求。</p>
<h3 data-id="heading-1">实现思路</h3>
<p>首先我们主要是要完成鼠标放在Modal框的头部部分时按住左键移动后对话框移动的一个效果。</p>
<p>这里我们要获取头部的元素并监听它的onmousedown方法，然后在onmousedown方法时通过计算对话框的高度宽度设定边界限制不让它移动到屏幕外，然后要监听document.onmousemove的方法计算鼠标移动的方向和距离，然后依据这个调整对话框的位置即可。</p>
<h3 data-id="heading-2">代码实现</h3>
<pre><code class="copyable">import Vue from 'vue'

// 弹窗拖拽属性
/**
 * @directive 自定义属性
 * @todo 弹窗拖拽属性
 * @desc 使用在弹窗内部任意加载的html添加v-drag
 * @param .ant-modal-header 弹窗头部用来拖动的属性
 * @param .ant-modal 拖动的属性
*/
Vue.directive('drag', (el, binding, vnode, oldVnode) => &#123;
  // inserted (el, binding, vnode, oldVnode) &#123;
  Vue.nextTick(() => &#123;
    const isThemeModal = el.classList.contains('grid-theme')
    const dialogHeaderEl = isThemeModal ? el.querySelector('.ant-tabs-bar') : document.querySelector('.ant-modal-header')
    const dragDom = isThemeModal ? el.querySelector('.ant-modal') : document.querySelector('.ant-modal')
    // dialogHeaderEl.style.cursor = 'move';
    dialogHeaderEl.style.cssText += ';cursor:move;'
    // dragDom.style.cssText += ';top:0px;'

    // 获取原有属性 ie dom元素.currentStyle 火狐谷歌 window.getComputedStyle(dom元素, null);
    const sty = (function () &#123;
      if (window.document.currentStyle) &#123;
        return (dom, attr) => dom.currentStyle[attr]
      &#125; else &#123;
        return (dom, attr) => getComputedStyle(dom, false)[attr]
      &#125;
    &#125;)()

    dialogHeaderEl.onmousedown = (e) => &#123;
      // 鼠标按下，计算当前元素距离可视区的距离
      const disX = e.clientX - dialogHeaderEl.offsetLeft
      const disY = e.clientY - dialogHeaderEl.offsetTop

      const screenWidth = document.body.clientWidth // body当前宽度
      const screenHeight = document.documentElement.clientHeight // 可见区域高度(应为body高度，可某些环境下无法获取)

      const dragDomWidth = dragDom.offsetWidth // 对话框宽度
      const dragDomheight = dragDom.offsetHeight // 对话框高度

      const minDragDomLeft = dragDom.offsetLeft
      const maxDragDomLeft = screenWidth - dragDom.offsetLeft - dragDomWidth - (isThemeModal ? 10 : 0)

      const minDragDomTop = dragDom.offsetTop
      const maxDragDomTop = screenHeight - dragDom.offsetTop - dragDomheight - (isThemeModal ? 10 : 0)

      // 获取到的值带px 正则匹配替换
      let styL = sty(dragDom, 'left')
      let styT = sty(dragDom, 'top')

      // 注意在ie中 第一次获取到的值为组件自带50% 移动之后赋值为px
      if (styL.includes('%')) &#123;
        // eslint-disable-next-line no-useless-escape
        styL = +document.body.clientWidth * (+styL.replace(/\%/g, '') / 100)
        // eslint-disable-next-line no-useless-escape
        styT = +document.body.clientHeight * (+styT.replace(/\%/g, '') / 100)
      &#125; else &#123;
        styL = +styL.replace(/\px/g, '')
        styT = +styT.replace(/\px/g, '')
      &#125;;

      document.onmousemove = function (e) &#123;
        // 通过事件委托，计算移动的距离
        let left = e.clientX - disX
        let top = e.clientY - disY

        // 边界处理
        if (-(left) > minDragDomLeft) &#123;
          left = -(minDragDomLeft)
        &#125; else if (left > maxDragDomLeft) &#123;
          left = maxDragDomLeft
        &#125;

        if (-(top) > minDragDomTop) &#123;
          top = -(minDragDomTop)
        &#125; else if (top > maxDragDomTop) &#123;
          top = maxDragDomTop
        &#125;
        // 移动当前元素
        dragDom.style.cssText += `;left:$&#123;left + styL&#125;px;top:$&#123;top + styT&#125;px;`
      &#125;

      document.onmouseup = function (e) &#123;
        document.onmousemove = null
        document.onmouseup = null
      &#125;
    &#125;
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">组件调用</h3>
<p>a-modal组件设置v-drag即可</p>
<pre><code class="copyable">...
<a-modal v-model="visible" title="提示" :maskClosable="false" @cancel="handleCancle" @ok="handleOk" v-drag>
  <p>确定删除字段吗</p>
</a-modal>
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">实现效果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fa8fffb02e5463d843cfae782d9b83b~tplv-k3u1fbpfcp-watermark.image" alt="v-drag.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<br>
<br>
~~ 感谢观看
<br>
<br>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<div align="center">关注下方【大前端驿站】</div>
<div align="center">让我们一起学，一起进步</div>
<p><strong>【分享、点赞、在看】三连吧，让更多的人加入我们</strong></p></div>  
</div>
            