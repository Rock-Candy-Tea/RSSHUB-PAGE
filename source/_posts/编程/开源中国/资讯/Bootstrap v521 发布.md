
---
title: 'Bootstrap v5.2.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4745'
author: 开源中国
comments: false
date: Fri, 09 Sep 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4745'
---

<div>   
<div class="content">
                                                                                            <p>Bootstrap v5.2.1 现已发布，这是一个补丁版本，主要包含了一些错误修复、文档更新和依赖性更新。</p> 
<h4><strong>Key changes</strong></h4> 
<p>更新了 calc() 函数，以解决 postcss-values-parser 中的一个明显的 bug，该 bug 导致源 Sass 文件在使用 React 和 PostCSS 构建时无法正常编译。解决方法是颠倒在 calc() 函数中的乘法顺序。用户可能需要根据自己的自定义进行类似的修改。</p> 
<p>还解决了一些长期存在的关于 button focus 和 active styling 的问题，特别是对于复选框和单选按钮。在移动设备上，input-based buttons 难以摆脱其 focus styles。这个问题在 v5.2.1 中得到了解决，开发团队将 .btns 的 :focus 改为 :focus-visible。现在，复选框和单选按钮在 :focus-visible 时不再改变它们的背景颜色，它们也不会收到 :hover styling。常规的 .btns 仍然有它们熟悉的 hover 和 focus styles。</p> 
<h4><strong>Highlights</strong></h4> 
<p><span style="background-color:#ffffff; color:#212529">除了上述更改之外，还修复了多个组件的错误：</span></p> 
<ul> 
 <li><strong>Accordion</strong> 
  <ul> 
   <li>更新<code>color</code>值以使用<code>$accordion-button-color</code>Sass 变量而不是 color contrast 函数</li> 
  </ul> </li> 
 <li><strong>Buttons</strong> 
  <ul> 
   <li>为按钮添加了透明的默认悬停边框颜色 CSS 变量，以修复视觉回归问题</li> 
   <li><code>$enable-gradients</code>设置为<code>true</code>时<code>.btn-link</code>不再有渐变</li> 
  </ul> </li> 
 <li><strong>Forms</strong> 
  <ul> 
   <li>Input groups 已更新<code>z-index</code>值以确保正确呈现经过验证的表单字段</li> 
   <li>Floating labels 现在重新设置了文本对齐方式，以确保风格一致。</li> 
  </ul> </li> 
 <li><strong>List Groups</strong> 
  <ul> 
   <li>只有一个 child 的水平列表组现在呈现正确的<code>border-radius</code></li> 
   <li>修改了<code>list-group-item</code>选择器以更好地支持 Bootstrap CSS 的嵌套导入</li> 
  </ul> </li> 
 <li><strong>Modals</strong> 
  <ul> 
   <li>更新了事件监听器以忽略滚动条点击、从<code>.modal-dialog</code>内部开始但在外部结束的点击，以及对在<code>.modal-dialog</code>外开始和结束的点击的响应。</li> 
  </ul> </li> 
 <li><strong>Pagination</strong> 
  <ul> 
   <li>修复了分页组件内的错误的<code>border-radius</code>值</li> 
  </ul> </li> 
 <li><strong>Scrollspy</strong> 
  <ul> 
   <li>Scrollspy 阈值选项现在可配置</li> 
  </ul> </li> 
 <li><strong>工具提示和弹出框</strong> 
  <ul> 
   <li>恢复了一些工具提示插件更新，以防止<code>selector</code>、dynamic content 和使用<span style="background-color:#ffffff; color:#212529"><span> </span></span><code>title</code>的工具提示出现问题</li> 
   <li>修复<span style="background-color:#ffffff; color:#212529"><span> </span></span><code>trigger</code>：调用<code>toggle()</code>时"manual"显示和立即隐藏的问题</li> 
  </ul> </li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>依赖项</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li>更新了 Autoprefixer 以修复<code>color-adjust</code>属性的警告问题</li> 
</ul> 
<p> 更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.getbootstrap.com%2F2022%2F09%2F07%2Fbootstrap-5-2-1%2F" target="_blank">查看官方博客</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            