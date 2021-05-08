
---
title: 'layui 2.6.6 发布，原生态 Web UI 组件库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6413'
author: 开源中国
comments: false
date: Sat, 08 May 2021 14:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6413'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次更新日志</p> 
<ul> 
 <li>[优化] layer 组件容器构建的核心代码，以解决自 2.6.0 以来在特殊场景下存在的某些异常问题</li> 
 <li>[优化] layer 组件当点击最小化时，让遮罩消失，窗口还原时恢复遮罩</li> 
 <li>[新增] layer 组件的 minStack 参数，用于控制最小化后是否默认堆叠在左下角</li> 
 <li>[新增] element nav 组件水平导航的子级菜单的两种对齐方式：右对齐，居中对齐</li> 
 <li>[新增] element nav 组件的 lay-bar="disabled" 属性，用于禁用滑块跟随功能</li> 
 <li>[优化] element nav 组件各种样式细节，其中包括下拉图标、子菜单等</li> 
 <li>[优化] element nav 组件在垂直导航场景时的滑块跟随功能</li> 
 <li>[优化] element tab 组件 tabAdd 方法，可将任意额外参数 &#123;key&#125; 组成 lay-&#123;key&#125;="&#123;value&#125;" 属性</li> 
 <li>[优化] element tab 组件当标题栏包含 a 标签时，点击 tab 切换，但未触发 a 标签跳转的问题</li> 
 <li>[新增] laydate 组件的 isPreview 参数，用于控制是否显示当前选择值的预览（默认 true）</li> 
 <li>[优化] laydate 组件的日期范围选择，因左右日期面板独立，固取消范围区间标注，增加开始-结束文本预览</li> 
 <li>[优化] laydate 组件的 range 参数，可支持传入数组，用于分别指定开始日期和结束日期的选择器</li> 
 <li>[优化] laydate 组件的时间范围选择，初始结束时间为 23:59:59</li> 
 <li>[优化] laydate 组件的当前日期不在设定的最小（min）和最大（max）日期内，则自动校正面板可选的初始日期</li> 
 <li>[优化] laydate 组件的选中完毕的赋值逻辑，对非 input 元素，如果存在子元素，则不进行默认赋值操作，由回调去处理</li> 
 <li>[优化] laydate 组件之前版本一直存在的初始处全局事件重复绑定的问题</li> 
 <li>[修复] laydate 组件当开启范围选择，未触发 change 回调的问题</li> 
 <li>[修复] laydate 组件在 ie11 因 laydate-day-mark 的 height：100% 导致的异常</li> 
 <li>[优化] upload 组件的多文件上传，可更好的对每个文件显示上传进度</li> 
 <li>[优化] flow 组件的 flow.lazyimg() 方法，对图片懒加载支持占位图显示（占位图 src，预加载图 lay-src）</li> 
 <li>[优化] util 组件的 util.toDateString((msec, format) 方法，可对第一个参数进行自动纠正和毫秒数无效的提示</li> 
 <li>[新增] 对名为 LAYUI_GLOBAL 的全局对象的识别，当对 layui.js 本身进行动态加载等特殊场景下，可通过该对象更好地解决部分组件依赖文件（css）的路径问题</li> 
 <li>[优化] 底层 layui.each() 核心代码</li> 
 <li>[优化] layout admin 大框架布局，可适配各个终端</li> 
 <li>[提示] Google 在近期发布的 Chrome v90 第三个维护版本 Chrome 90.0.4430.93，修复了上两个版本因关闭打印窗口导致的浏览器卡顿问题（之前 layui table 的打印亦受此影响）</li> 
</ul>
                                        </div>
                                      
</div>
            