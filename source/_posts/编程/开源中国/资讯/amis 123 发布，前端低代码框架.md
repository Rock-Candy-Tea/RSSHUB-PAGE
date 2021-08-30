
---
title: 'amis 1.2.3 发布，前端低代码框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8354'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 10:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8354'
---

<div>   
<div class="content">
                                                                                            <p>amis 1.2.3 已经发布，前端低代码框架。</p> 
<p>此版本更新内容包括：</p> 
<h2>Feature ✨</h2> 
<ul> 
 <li>InputNumber 支持只读属性 (#2450) @qinhaoyan</li> 
 <li>新增 InputText、Textarea 字数统计功能 (#2431) <a href="https://www.oschina.net/2betop">@2betop </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/form/input-text#%E6%98%BE%E7%A4%BA%E8%AE%A1%E6%95%B0%E5%99%A8" target="_blank">文档</a> <a href="https://baidu.gitee.io/amis/zh-CN/components/form/textarea#%E6%98%BE%E7%A4%BA%E8%AE%A1%E6%95%B0%E5%99%A8" target="_blank">文档</a></li> 
 <li>按钮、链接、模板、图表支持角标; 角标支持动画效果 (#2427) <a href="https://www.oschina.net/nwind">@nwind </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/badge" target="_blank">文档</a></li> 
 <li>日期、时间、富文本支持 <code>borderMode</code> (#2401) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>InputNumber 增加 <code>prefix</code>、<code>subfix</code>、<code>kilobitSeparator</code>、<code>borderMode</code> 属性 (#2399) @qinhaoyan <a href="https://baidu.gitee.io/amis/zh-CN/components/form/input-number#%E5%89%8D%E5%90%8E%E7%BC%80-%E5%8D%83%E5%88%86%E5%88%86%E9%9A%94" target="_blank">文档</a></li> 
 <li>Select 组件增加 <code>hideSelected</code> 属性，是否隐藏已选选项 (#2396) @qinhaoyan</li> 
 <li>新增 年份范围 InputYearRange (#2390) <a href="https://www.oschina.net/allenve">@Allen </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/form/input-year-range" target="_blank">文档</a></li> 
 <li>InputText 支持前缀、后缀 (#2386) <a href="https://www.oschina.net/allenve">@Allen </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/form/input-text#%E5%89%8D%E7%BC%80%E5%92%8C%E5%90%8E%E7%BC%80" target="_blank">文档</a></li> 
 <li>inputText, Textarea, Select 支持配置 <code>borderMode</code> 包括,全边框,半边框,无边框 (#2375) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>Grid & Hbox 支持 <code>gap</code>,<code>hAlign</code>, <code>vAlign</code> 配置 (#2373) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>Button-Group 支持平铺样式 (#2371) <a href="https://www.oschina.net/2betop">@2betop </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/button-group#%E5%B9%B3%E9%93%BA%E6%A8%A1%E5%BC%8F" target="_blank">文档</a></li> 
 <li>Web-Component 组件 (#2368) <a href="https://www.oschina.net/nwind">@nwind </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/web-component" target="_blank">文档</a></li> 
 <li>升级 Json 组件，支持查看并修改功能 (#2360) <a href="https://www.oschina.net/2betop">@2betop </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/json#%E5%BC%80%E5%90%AF-json-%E4%BF%AE%E6%94%B9" target="_blank">文档</a></li> 
 <li>新增 Input-Time-Range 时间范围组件 (#2340) <a href="https://www.oschina.net/allenve">@Allen </a> <a href="https://baidu.gitee.io/amis/zh-CN/components/form/input-datetime-range" target="_blank">文档</a></li> 
</ul> 
<h2>Enhancement</h2> 
<ul> 
 <li>调整 Dialog 动作的 <code>reload</code> 优先级 (#2445) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>补充部分 <code>locale</code> (#2438) @RickCole21</li> 
 <li>优化 Tabs 成员的 <code>key</code> (#2436) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>添加 Checkboxes 全选/不选 多语言 (#2433) @Vokinloksar</li> 
 <li>Input-Sub-Form 功能补充及样式优化 (#2429) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>Condition-Builder 支持字段进行搜索 (#2383) @zhyc9de</li> 
 <li>升级 monaco-editor (#2421) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>调整 Image 和 Carousel (#2412) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>调整弹框中查找子节点渲染器处理动作逻辑 (#2410) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>修复换默认主题导致的单元测试报错 (#2409) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li><code>itemActions</code> 配置后工具栏在没有勾选的情况下也展示但是处于禁用态 (#2406) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>调整云舍成为默认主题，之前的默认主题改名 ang (#2404) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>优化 InputTable <code>columns</code> 中直接用表单项的情况 (#2398) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>InputTable 优化升级 (#2394) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>Each 组件优化 (#2392) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>Input-Image 优化 (#2382) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>Condition-Builder 新增英文本地化 (#2378) @zhyc9de</li> 
 <li>优化 InputRange 中间值位置 (#2374) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>将 cfc 的 mock 接口放到项目中支持文档离线访问；将大部分图片外联都放入项目中管理 (#2366) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>表单报错信息中增加所有表单项的报错信息 (#2357) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>优化 Group 相关样式 (#2348) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
</ul> 
<h2>Bugfix</h2> 
<ul> 
 <li>修复编译成 es5 后 WebComponent 报错 (#2452) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>修复 Combo 中配置 <code>clearValueOnHidden</code> 无法删除 item 问题 (#2454) @RickCole21</li> 
 <li>修复 Tree 组件节点勾选异常问题 (#2449) @RickCole21</li> 
 <li>修复 withRemoteConfig 实现的自动刷新无法关闭问题 (#2448) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>修复 mst 报错问题 (#2446) @RickCole21</li> 
 <li>修复 inputNumber 组件直接操作增减报错问题 (#2444) @qinhaoyan</li> 
 <li>修复 Service 组件 <code>silentPolling</code> 失效问题 (#2443) @RickCole21</li> 
 <li>修复 Input-Datetime 组件 <code>minDate</code> 和 <code>maxDate</code> 失效问题 (#2442) @RickCole21</li> 
 <li>修复 Iframe 获取变量时，自动 escape 的问题 (#2441) @RickCole21</li> 
 <li>修复 DiffEditor 撤销问题 (#2440) @RickCole21</li> 
 <li>修复 Input-Rating <code>allowClear</code> 问题 (#2437) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>修复 Picker 无法自动选中的问题 (#2430) @RickCole21</li> 
 <li>修复 WrapControl 数据域问题 (#2423) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>修复 isJson 校验 (#2416) <a href="https://www.oschina.net/anonymity94">@Anonymity94 </a></li> 
 <li>修复导入 default 会报错问题 (#2408) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>避免 npm 默认主题引用失败 (#2405) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>富文本编辑器 <code>tinymce</code> 模式上传图片问题 (#2395) <a href="https://www.oschina.net/allenve">@Allen </a></li> 
 <li>解决 Combo 的 <code>unique</code> 属性当字段值为数字 <code>0</code>, <code>false</code>, <code>空字符串</code>的时候，不走<code>unique</code>校验的逻辑 (#2393) @sarding</li> 
 <li>修复 CRUD 在翻页时 <code>page/perPage</code> 会变成字符串问题 (#2376) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>修复 选项类表单项直接放在 Form 外面不可用的问题 (#2370) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>修复 Form 表单项验证器的<code>this</code> 指向问题 (#2367) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>使用 mpegtsjs 替换 flvjs，修复音视频可能不同步等问题 (#2358) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/baidu/amis/releases/1.2.3">https://gitee.com/baidu/amis/releases/1.2.3</a></p>
                                        </div>
                                      
</div>
            