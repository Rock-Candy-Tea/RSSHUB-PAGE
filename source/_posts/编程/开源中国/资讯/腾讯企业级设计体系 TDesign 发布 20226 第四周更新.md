
---
title: '腾讯企业级设计体系 TDesign 发布 2022.6 第四周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1958'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1958'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一 / 多端覆盖 / 跨技术栈的企业级前端应用。</p> 
<p style="margin-left:0px">目前，TDesign 发布了 2022 年 6 月的第四周更新，带来如下变更：</p> 
<h2 style="margin-left:0px"><strong>组件库</strong></h2> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.43.0" target="_blank"><strong>0.43.0</strong></a></h2> 
<h3><strong>❗ Breaking Changes</strong></h3> 
<ul> 
 <li>默认移除全局 reset 样式引入，可从 <code>tdesign-vue/dist/reset.css </code>中单独引入，存在不兼容更新</li> 
 <li><code>DatePicker</code>: 重构<code>DatePicker</code>为composition API，全新的UI样式及交互，新增DateRangePicker组件，替换此前的range写法 ，存在不兼容更新</li> 
 <li><code>TimePicker</code>: 重构<code>TimePicker</code>为composition API，全新的UI样式及交互，<code>disableTime </code>API有所调整，存在不兼容更新</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Space</code>: 新增 space 组件</li> 
 <li><code>ConfigProvider</code>: 增加 <code>input </code>组件 <code>autocomplete </code>配置，增加 <code>dialog </code>组件 <code>closeOnEscKeydown</code>, <code>closeOnOverlayClick </code>配置, 增加 <code>select</code> 组件 <code>filterable</code> 配置，增加 <code>drawer </code>组件 <code>closeOnEscKeydown</code>, <code>closeOnOverlayClick </code>配置</li> 
 <li><code>Local</code>: 增加日语和韩语语言包</li> 
 <li><code>Table</code>: fullRow不参与排序</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Table</code>: 
  <ul> 
   <li>吸顶表头支持自定义滚动容器</li> 
   <li>处理<code>table</code>在部分SSR场景渲染失败的问题</li> 
   <li>修复仅有<code>firstFullRow</code>不渲染的问题</li> 
   <li>修复<code>paginationAffixedBottom </code>透传<code>Affix </code>参数不生效</li> 
   <li>修复 0.41.7 版本后过滤功能构建后异常的问题</li> 
   <li>修复 0.41.7 版本后过滤功能构建后异常的问题</li> 
  </ul> </li> 
 <li><code>Select</code>: 
  <ul> 
   <li><code>option</code>数量小于<code>threshold</code>时不开启虚拟滚动</li> 
   <li>单选下 valueType 为 object 时, onChange返回值类型修复</li> 
   <li>修复 useDefaultValue、useVModel 初值为 undefined 时, 组件初始化为非受控的问题</li> 
   <li>修复多选下换行提取占满一行的问题</li> 
  </ul> </li> 
 <li><code>SelectInput</code>: 修复展开下拉时失去焦点不高亮的问题</li> 
 <li><code>TagInput</code>: 修复中文输入按下 Enter 时不触发新标签</li> 
 <li><code>InputNumber</code>: 修复<code>enter</code>事件不触发的问题</li> 
 <li><code>Affix</code>: 节点挂载后吸顶没有执行的问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.43.0" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.43.0</a></p> 
<h2><strong>Vue3 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.16.1" target="_blank"><strong>0.16.1</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Cascader</code>： 支持 <code>filter API</code> 用于自定义搜索方法</li> 
 <li><code>Form</code>： 新增 <code>validateOnly </code>实例方法</li> 
 <li><code>Form</code>： 新增 <code>validate</code>、<code>submit </code>实例方法参数 <code>showErrorMessage</code></li> 
 <li><code>Dialog</code>： 新增<code>preventScrollThrough</code></li> 
 <li><code>Table</code>： 支持拖拽调整宽度，设置 <code>resizable=true</code> 即可</li> 
 <li><code>Table</code>： 支持表头吸顶、表尾吸底、滚动条吸底、分页器吸底等</li> 
 <li><code>Table</code>： 树形结构，<code>appendTo </code>支持添加多条数据</li> 
 <li><code>Table</code>： 树形结构，支持数据节点 懒加载 子节点数据</li> 
 <li><code>Icon</code>： 新增<code>rollfront</code>图标</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>DatePicker</code>： 修复 <code>datepicker format</code> 导致的高亮问题</li> 
 <li><code>TimePicker</code>： 修复在 <code>datepicker </code>中混用 不保留修改结果二次打开的异常</li> 
 <li><code>TimePicker</code>： 修复部分情况下由于<code> allowInput ref</code> 问题导致保留改动结果的错误</li> 
 <li><code>DatePicker</code>： 修复通过过快捷方式设置的时间区间高亮数据异常</li> 
 <li><code>DatePicker</code>： 修复栅格的情况下组件宽度 超过父级容器的限制 组件显示不完整</li> 
 <li><code>Dialog</code>： 修复 dialog 蒙层点击事件失效</li> 
 <li><code>Select</code>： 修复使用 <code>onEnter </code>事件报错</li> 
 <li><code>Select</code>： 修复远程搜索功能失效了</li> 
 <li><code>Cascader</code>： 修复可过滤情况下，结果为空时候的 <code>popup </code>宽度问题</li> 
 <li><code>Input</code>： 修复 <code>type </code>为 <code>password </code>时 <code>clearable </code>属性不生效</li> 
 <li><code>Form</code>： <code>submit </code>和 reset 现在不会触发 submit 和 reset 事件</li> 
 <li><code>Form</code>： <code>submit </code>实例方法兼容 safari 浏览器 (https：//github.com/<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Fpull%2F964" target="_blank">Tencent/tdesign-vue-next/pull/964</a></li> 
 <li><code>ConfigProvider</code>： 修复 <code>inject </code>在 <code>computed </code>中意外出现, 优化配置文件 <code>merge </code>性能</li> 
 <li><code>Tabs</code>： 修复 <code>panels </code>变化时，往右按钮不出现的问题</li> 
 <li><code>Table</code>： 支持动态数据合并单元格</li> 
 <li><code>Table</code>： 吸顶表头和自定义显示列场景，支持列拖拽调整顺序</li> 
 <li><code>Table</code>： 修复 <code>firstFullRow </code>存在时，拖拽排序的顺序不正确问题</li> 
 <li><code>Table</code>： 修复加载更多的加载组件尺寸异常问题</li> 
 <li><code>TimePicker</code>： <code>range </code>组件最外层使用 <code>range-picker</code> 命名与单时间选项区分</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.16.1" target="_blank">https://github.com/Tencent/tdesign-vue-next/releases/tag/0.16.1</a></p> 
<h2><strong>React for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.36.1" target="_blank"><strong>0.36.1</strong></a></h2> 
<h3><strong>❗ Breaking Changes</strong></h3> 
<ul> 
 <li><code>reset</code>： 默认移除全局 reset 样式引入，可从 <code>tdesign-react</code>/<code>dist/reset.css</code> 中单独引入，存在不兼容更新</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Space</code>： 新增 Space 组件</li> 
 <li><code>taginput</code>： <code>excessTagsDisplayType </code>默认值更为 <code>break-line</code></li> 
 <li><code>Table</code>： <code>firstFullRow</code>不参与排序</li> 
 <li><code>Form</code>： 支持 <code>validateOnly </code>函数 & <code>validate </code>函数支持 <code>showErrorMessage </code>参数</li> 
 <li><code>Locale</code>： 新增日文韩文翻译</li> 
 <li><code>Select</code>： label 支持 TNode 类型</li> 
 <li><code>ConfigProvider</code>： 增加 <code>input</code> 组件 <code>autocomplete </code>配置，增加 <code>dialog</code> 组件 <code>closeOnEscKeydown</code>, <code>closeOnOverlayClick </code>配置, 增加 <code>select</code> 组件 <code>filterable</code> 配置，增加 <code>drawer</code> 组件 <code>closeOnEscKeydown</code>, <code>closeOnOverlayClick </code>配置</li> 
 <li><code>Icon</code>： 新增<code>rollfront</code>图标</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>table</code>： 修复加载更多的加载组件尺寸异常问题</li> 
 <li><code>Select</code>： 修复输入部分特殊符号过滤时组件崩溃的问题</li> 
 <li><code>Table</code>： 修复仅有<code>firstFullRow</code>渲染为空的问题</li> 
 <li><code>Select</code>： <code>onChange</code>事件回调参数缺失</li> 
 <li><code>Form</code>： 修复 <code>number </code>校验无效问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.36.1" target="_blank">https://github.com/Tencent/tdesign-react/releases/tag/0.36.1</a></p> 
<h2 style="margin-left:0px"><strong>解决方案及周边</strong></h2> 
<h2><strong>TDesign Starter CLI 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-starter-cli%2Freleases%2Ftag%2F0.2.4" target="_blank"><strong>0.2.4</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>自定义模式下移除无效的引用</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-starter-cli%2Freleases%2Ftag%2F0.2.4" target="_blank">https://github.com/Tencent/tdesign-starter-cli/releases/tag/0.2.4</a></p> 
<h2><strong>TDesign Vue Next Starter 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next-starter%2Freleases%2Ftag%2F0.3.5" target="_blank"><strong>0.3.5</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>调整类型相关问题的项目结构</li> 
 <li>改造请求封装相关代码</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>修复首页<code>TAB</code>关闭其他时的异常</li> 
 <li>修复升级 0.16 版本后自定义设置中选项样式的异常<br> 详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next-starter%2Freleases%2Ftag%2F0.3.5" target="_blank">https://github.com/Tencent/tdesign-vue-next-starter/releases/tag/0.3.5</a></li> 
</ul> 
<h2><strong>TDesign React Starter 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react-starter%2Freleases%2Ftag%2F0.1.5" target="_blank"><strong>0.1.5</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>新增卡片列表页</li> 
 <li>菜单路由配置<code>hidden</code>和<code>single</code>功能</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>同步<code>DatePicker</code>组件升级的改动</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react-starter%2Freleases%2Ftag%2F0.1.5" target="_blank">https://github.com/Tencent/tdesign-react-starter/releases/tag/0.1.5</a></p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv2022.6.27" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v2022.6.27</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            