
---
title: '📧叮~你有一份 DevUI 12 新版本待查收~😋'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-332f8ae87d9473fb9aadb43853f2b5fcec3.png'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 23:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-332f8ae87d9473fb9aadb43853f2b5fcec3.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <p><img alt src="https://oscimg.oschina.net/oscnet/up-332f8ae87d9473fb9aadb43853f2b5fcec3.png" referrerpolicy="no-referrer"></p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a>是面向企业中后台产品的开源前端解决方案，其设计价值观基于"至简"、"沉浸"、"灵活"三种自然与人文相结合的理念，旨在为设计师、前端开发者提供标准的设计体系，并满足各类落地场景，是一款企业级开箱即用的产品。如果你正在开发 ToB 的工具类产品，DevUI 将是一个很不错的选择！</p> 
  <p>DevUI是一款基于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fdesign-cn%2Fstart" target="_blank">DevUI Design</a>设计规范的Angular组件库，开源于2019年，已经持续维护2年时间，沉淀了61个组件，其中有不少都是业界组件库没有的特色组件。</p> 
  <p>前面预告了两次，今天 DevUI 12 版本终于来了！升级了最新的 Angular 12 版本，让我们一起来看看还有哪些新特性吧！</p> 
  <h1>DevUI 12：全面支持 Angular Ivy 新引擎</h1> 
  <h2>新特性</h2> 
  <ol> 
   <li>规范化组件间距，变更为4的倍数以更好兼容缩放等计算后的展示效果</li> 
   <li>Select支持多选模式下回车选中/取消选中</li> 
   <li>TreeSelect支持自定义已选中项模板，支持通过设置checkRelation控制父子节点的选中关系</li> 
   <li>Upload支持选择文件夹上传，单文件上传成功后保留文件显示</li> 
   <li>Cascader支持设置appendTobody</li> 
   <li>Button优化设置宽度后文字过长超出显示范围</li> 
  </ol> 
  <h2>Bug修复</h2> 
  <ol> 
   <li>TreeSelect修复多选模式下设置treeNodeIdKey后无法删除节点的问题</li> 
   <li>DataTable修复拖拽中容易失焦的问题</li> 
   <li>dragDrop修复无主题设置场景下placeholder无颜色的问题</li> 
   <li>Editorx中文输入法下光标定位等问题修复</li> 
   <li>Tree修复调用checkAllNodes方法无法改变半选状态的问题</li> 
   <li>TagsInput修复标签过长无法删除的问题</li> 
  </ol> 
  <p>完整Changelog：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui%2Freleases%2Ftag%2F12.0.0" target="_blank">12.0.0版本Changelog</a></p> 
  <h1>特色组件展播</h1> 
  <h2>Datepicker Pro 日期选择器</h2> 
  <p>组件链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2FdatepickerPro%2F" target="_blank">https://devui.design/components/zh-cn/datepickerPro/</a></p> 
  <h3>特点介绍</h3> 
  <p>Datepicker Pro组件借鉴移动端，利用鼠标滚轮操作范围选择，附加精准位置点击，减少用户的点击次数，缩短用户对于时间选择的操作路径。</p> 
  <h3>功能详情</h3> 
  <ol> 
   <li>组件提供了单选/范围类型，支持日期/周/月份/年份的模式，支持各种自定义模板扩展，充分满足业务复杂场景</li> 
   <li>提供日历面板形式，用户可自定义嵌入各类型场景，灵活使用</li> 
  </ol> 
  <p><img alt="datepickerPro.gif" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e7baf61108c451da62352c1679c0fe0~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
  <p>更详细的介绍可以参考我们之前的文章：</p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6984312544894648334" target="_blank">DevUI 11.4.0 发布：DatePickerPro来啦</a></p> 
  <h2>Category Search 分类搜索</h2> 
  <p>组件链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fcategory-search%2F" target="_blank">https://devui.design/components/zh-cn/category-search/</a></p> 
  <h3>特点介绍</h3> 
  <p>Category Search组件将高频常用的搜索过滤内容聚合到一个组件中，形成符合搜索过滤的操作模型，减少页面冗余的搜索过滤条件的呈现，进而降低用户的理解和使用成本</p> 
  <h3>功能详情</h3> 
  <p>组件提供多场景菜单模式，不同操作模式下，菜单的展示内容不同：</p> 
  <ol> 
   <li>默认提供类别信息</li> 
   <li>存在类别选中项时，展示该类别的选项详情</li> 
   <li>输入框存在搜索文本，展示符合文本的搜索分类或分类下符合条件的选项</li> 
  </ol> 
  <p>组件提供一键清空，过滤器保存，类别过多的列表展示，最大程度兼容各类复杂的业务场景</p> 
  <p><img alt="categorySearch.gif" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29f496886d9243b1a6980663bf164ed1~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
  <p>更详细的介绍可以参考我们之前的文章：</p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6956612556710477860" target="_blank">CategorySearch分类搜索组件初体验</a></p> 
  <h2>Quadrant Diagram 象限图</h2> 
  <p>组件链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fquadrant-diagram%2F" target="_blank">https://devui.design/components/zh-cn/quadrant-diagram/</a></p> 
  <h3>特点介绍</h3> 
  <p>象限图经常用于规划事件的优先级，用于分析处理数据与期望的偏离程度等。组件通过拖拽，实现对目标的位置掌控及信息呈现。</p> 
  <h3>功能详情</h3> 
  <ol> 
   <li>组件通过与拖拽的联动，坐标跟随线的定位，可以轻松实现标签的移动，便于使用者进行数据的变更，掌控事项的发展；</li> 
   <li>组件内置了功能区域，提供标签的放大，缩小及象限图全屏的功能；</li> 
   <li>灵活的样式定制能力，用户可根据自己的诉求灵活搭配。</li> 
  </ol> 
  <p><img alt="quadrantDiagram.gif" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d79e96adf0b49ae861579cf0bf8aac5~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6844904169665462280" target="_blank">手把手教你如何使用象限图组件</a></p> 
  <h2>Gantt 甘特图</h2> 
  <p>组件链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fgantt%2F" target="_blank">https://devui.design/components/zh-cn/gantt/</a></p> 
  <h3>特点介绍</h3> 
  <p>甘特图常用于多个事务进度的跟踪与管理，每个项目以条状图的形式显示，进度与其他时间相关的进展的内在关系以可视化形式进行显示。</p> 
  <h3>功能详情</h3> 
  <ol> 
   <li>基本图形形式呈现，以时间维度显示每个条目之间内在联系，支持bar、bar-parent、milestone三种不同形式条状展示；</li> 
   <li>多种交互支持：条目拖拽、进度更新、时间范围更新、快捷跳转、视图变化、全屏等；</li> 
   <li>与table搭配：可与datatable搭配使用，进行更丰富维度信息呈现与管理。</li> 
  </ol> 
  <p><img alt="gantt.gif" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414371de0ac847b9acf832c879c9b9fb~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
  <h1>致谢</h1> 
  <p>感谢对DevUI组件库给予帮助的开发者们，祝大家使用愉快~</p> 
  <h1>预告</h1> 
  <blockquote> 
   <p>DevUI Admin 2.0 版本也将在本月17号重磅发布，提供了一项神奇的黑科技，让我们拭目以待吧！</p> 
  </blockquote> 
  <p>也欢迎大家参与到DevUI生态的建设中来，目前 DevUI 开源生态主要有以下产品：</p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">NG DevUI</a>：基于DevUI Design设计规范的Angular组件库</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Ficon%2FruleResource" target="_blank">DevUI Icons</a>：与DevUI组件库配套使用的字体图标库</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank">NG DevUI Admin</a>：开箱即用的企业级中后台管理系统</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2FDevUIHelper" target="_blank">DevUI Helper</a>：一款VSCode插件，DevUI代码助手，给你带来丝滑的代码补全体验。</li> 
   <li><a href="https://gitee.com/devui/vue-devui">Vue DevUI</a>：vue3版本DevUI组件库，支持PC/Mobile（目前还在孵化中，欢迎参与建设~）</li> 
  </ul> 
 </div> 
</div>
                                        </div>
                                      
</div>
            