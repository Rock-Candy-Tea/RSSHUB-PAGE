
---
title: '最简单、最好用、最好玩的 Blazor UI 库 BootstrapBlazor  v5.0.23 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-741827e9785fc305c3a25fe8f82e8c0a41b.png'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 13:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-741827e9785fc305c3a25fe8f82e8c0a41b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:center">Bootstrap Blazor 组件库 </h1> 
<div style="text-align:left"> 
 <h2 style="text-align:center">一套基于 Bootstrap 和 Blazor 的企业级组件库 </h2> 
</div> 
<h2 style="text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-741827e9785fc305c3a25fe8f82e8c0a41b.png" referrerpolicy="no-referrer"> </h2> 
<h2 style="text-align:left">本期更新 </h2> 
<blockquote> 
 <h4 style="text-align:start">增加功能 </h4> 
 <ul> 
  <li> <p>!1242 feat(#I3EIU2):  <code>InputNumber </code> 步长默认值微调 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1242">#I3EIU2</a> </p> 
   <ol> 
    <li> <code>short </code>  <code>int </code>  <code>long </code> 默认步长  <code>Step </code> 等于  <code>1 </code></li> 
    <li> <code>single </code>  <code>double </code>  <code>decimal </code> 默认步长  <code>Step </code> 等于  <code>0.01 </code></li> 
   </ol> </li> 
  <li> <p>!1238 feat(#I3D6UP): 更新  <code>VadliateForm </code>  <code>EditForm </code>  <code>ValidateBase </code> 表单组件嵌套使用时  <code>ShowLabel </code> 逻辑 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1238">#I3D6UP</a> </p> 
   <ol> 
    <li>各种嵌套逻辑比较复杂详细情况请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.blazor.zone%2Flabels" target="_blank">https://www.blazor.zone/labels</a></li> 
   </ol> </li> 
  <li> <p>!1228 feat(#I3E183):  <code>VadliateForm </code> 组件支持异步操作按钮 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1228">#I3E183</a> </p> 
   <ol> 
    <li>验证表单内组件保存数据时提交到  <code>webapi </code> 中，为防止提交按钮多次点击 设置  <code>Button </code> 组件参数  <code>IsAsync </code> 即可</li> 
   </ol> </li> 
  <li> <p>!1227 feat(#I3DX9J):  <code>Markdown </code> 组件增加  <code>IsViewer </code> 属性 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1227">#I3DX9J</a> </p> 
   <ol> 
    <li>可用于将  <code>md </code> 文本显示为  <code>Html </code> 代码</li> 
   </ol> </li> 
  <li> <p>!1226 feat(#I3DZKZ):  <code>ToolbarButton </code>  <code>IsAsync </code> 仅控制自身 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1226">#I3DZKZ</a> </p> 
   <ol> 
    <li> <code>Table </code> 组件工具栏内按钮提供  <code>IsAsync </code> 功能，提供异步操作支持</li> 
    <li>此功能用于异步调用  <code>webapi </code> 等延时操作，防止用户多次点击</li> 
    <li>点击后禁用自身不影响其他按钮，操作完成后恢复</li> 
   </ol> </li> 
  <li> <p>!1224 feat(#I3DYJF): 更细表单组件内非必填项  <code>Label </code> 样式与必填项对齐 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1224">#I3DYJF</a> </p> </li> 
  <li> <p>!1220 feat(#I3DWIV):  <code>ToolbarButton </code> 工具栏按钮增加  <code>IsAsync </code> 属性用于异步操作禁用自身 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1220">#I3DWIV</a> </p> </li> 
  <li> <p>!1219 feat(#I3DWIO):  <code>ToastOptin </code> 弹窗配置项增加  <code>Close </code> 方法用于代码关闭  <code>Toast </code> 弹窗 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1219">#I3DWIO</a> </p> </li> 
  <li> <p>!1218 feat(#I3DVN9):  <code>EditDialog </code> 弹窗绑定模型时自动过滤  <code>Editable </code> 条件进行渲染 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1218">#I3DVN9</a> </p> </li> 
  <li> <p>!1214 feat(#I3DVAK):  <code>Button </code> 组件增加  <code>IsAsync </code> 参数 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1214">#I3DVAK</a> </p> 
   <ol> 
    <li>当按钮为异步请求按钮时，点击按钮后自身状态会改变为禁用状态，同时显示 LoadingIcon 小图标，异步请求结束后恢复正常</li> 
   </ol> </li> 
  <li> <p>!1213 feat(#I3DUHU):  <code>Table </code> 组件再特定条件下按钮可能会出现多份 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1213">#I3DUHU</a> </p> 
   <ol> 
    <li>使用代码控制  <code>Table </code> 工具栏按钮时导致按钮出现多份</li> 
   </ol> </li> 
  <li> <p>!1209 feat(#I3DTRL):  <code>CheckboxList </code> 组件增加  <code>IsDisabled </code> 禁用支持 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1209">#I3DTRL</a> </p> </li> 
  <li> <p>!1206 feat(#I3DN0R): 更新  <code>Upload </code> 组件，适配  <code>ValidateForm </code> 表单 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1206">#I3DN0R</a> </p> 
   <ol> 
    <li>增加  <code>Upload </code> 组件内置  <code>ValidateForm </code> 内后显示标签</li> 
    <li>增加  <code>Upload </code> 组件绑定模型字段有  <code>[Required] </code> 表示后自动增加  <code>* </code> 记号功能</li> 
    <li>增加  <code>Uplaod </code> 组件对禁用  <code>IsDisabled </code> 支持</li> 
   </ol> </li> 
  <li> <p>!1203 feat(#I3DF9O): Table 组件增加  <code>ShowResetSearch </code> 参数 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1203">#I3DF9O</a> </p> 
   <ol> 
    <li>用于控制  <code>清空搜索 </code> 按钮</li> 
   </ol> </li> 
  <li> <p>!1200 feat(#I3D7YR): 表单内标签自动添加  <code>* </code> 必填标记符号 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1200">#I3D7YR</a> </p> 
   <ol> 
    <li>绑定模型字段增加  <code>[Required] </code> 标签后自动增加  <code>* </code> 记号</li> 
   </ol> </li> 
  <li> <p>!1199 feat(#I3D71B): 公开 ServiceProviderHelper 静态扩展类 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1199">#I3D71B</a> </p> 
   <ol> 
    <li>提供静态类获取注入服务能力</li> 
    <li>获取服务与  <code>[Inject] </code> 标签相同</li> 
   </ol> </li> 
  <li> <p>!1197 feat(#I3CXJY): Select 组件内置对枚举类型的处理 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1197">#I3CXJY</a> </p> 
   <ol> 
    <li>绑定类型为枚举时，不需要再额外指定  <code>Items </code> 集合属性，内部自行构建</li> 
    <li>绑定类型可为空时，自动构建  <code>请选择 ... </code> 默认项，回落机制是优先查找  <code>placeholder </code> 如未提供则使用  <code>Select </code> 组件的资源文件</li> 
   </ol> </li> 
 </ul> 
 <h4 style="text-align:start">问题修复 </h4> 
 <ul> 
  <li> <p>!1243 fix(#I3EJHX): 修复  <code>Table </code> 组件在移动端显示行号时点击行行号一直增加问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1243">#I3EJHX</a> </p> </li> 
  <li> <p>!1241 fix(#I3EHKZ): 修复  <code>CheckboxList </code> 组件无内容是高度不合理问题 设置为 35px <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1241">#I3EHKZ</a> </p> </li> 
  <li> <p>!1237 fix(I3EG1S): 修复  <code>Avatar </code>  <code>Upload </code> 组件利用代码更改  <code>Url </code> 后，界面不刷新问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1237">#I3EG1S</a> </p> </li> 
  <li> <p>!1236 fix(I3EB63): 修复表单组件利用代码设置  <code>DisplayText=null </code> 后无法显示资源文件设置的文本问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1236">#I3EB63</a> </p> </li> 
  <li> <p>!1234 fix(I3EB4V): 修复  <code>ValidateForm </code> 组件代码更新  <code>Model </code> 后不触发  <code>OnValidaSumbit </code> 回调事件问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1234">#I3EB4V</a> </p> </li> 
  <li> <p>!1225 fix(I3DYX5): 修复  <code>Table </code> 组件过滤功能选择  <code>All </code> 条件时不触发重新查询问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1225">#I3DYX5</a> </p> </li> 
  <li> <p>!1223 fix(#I3DXDI): 修复  <code>Collapse </code> 组件点击  <code>Body </code> 空白地方导致全部展开问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1223">#I3DXDI</a> </p> </li> 
  <li> <p>!1216 fix(#I3DVN3): 修复  <code>SearchDialog </code> 绑定模型时未过滤  <code>Searchable </code> 条件问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1216">#I3DVN3</a> </p> </li> 
  <li> <p>!1208 fix(#I3DP5D): 修复  <code>Table </code> 组件编辑模式为  <code>EditForm </code> 时自动生成  <code>Editable </code> 参数不生效问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1208">#I3DP5D</a> </p> 
   <ol> 
    <li> <code>[AutoGenerateColumn(Editable=false)] </code> 标签不生效， <code>EditForm </code> 模式下编辑框内仍然显示该绑定字段</li> 
   </ol> </li> 
  <li> <p>!1198 fix(#I3DC8H): 自定义验证器缺失 ValidateContext 对象 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1198">#I3DC8H</a> </p> 
   <ol> 
    <li>表单组件使用自定义验证器时，缺少 ValidateContext 对象导致部分功能无法完成</li> 
   </ol> </li> 
 </ul> 
 <h4 style="text-align:start">示例更新 </h4> 
 <ul> 
  <li>!1244 docs(#I3EJIM): 更新  <code>Table </code> 组件行内自定义按钮点击后，选中本行示例 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1244">#I3EJIM</a></li> 
  <li>!1235 docs(#I3EB62): 更新  <code>Table </code> 组件表单维护示例代码 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1235">#I3EB62</a></li> 
  <li>!1231 docs(#I3E7HZ): 更新  <code>Table </code> 组件列示例代码 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1231">#I3E7HZ</a></li> 
  <li>!1229 docs(#I3E6RM): 更新  <code>Table </code> 组件列示例代码 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1229">#I3E6RM</a></li> 
  <li>!1221 docs(#I3DWJQ): 更新  <code>Table </code> 组件工具栏异步操作示例 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1221">#I3DWJQ</a></li> 
  <li>!1210 docs(#I3DTRQ): 增加  <code>Table </code> 组件自定义数据注入服务示例文档 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1210">#I3DTRQ</a></li> 
  <li>!1202 docs(#I3DECD): 更新  <code>Table </code> 组件数据导出示例文档 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1202">#I3DECD</a></li> 
  <li>!1201 docs(#I3DDGK): 更新  <code>Table </code> 组件 Filter 示例文档 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1201">#I3DDGK</a></li> 
 </ul> 
 <h4 style="text-align:start">性能优化 </h4> 
 <ul> 
  <li>!1240 refactor(#I3EHK7):  <code>EditorForm </code> 组件级联参数更改为自身保证表单组件  <code>ShowLabel </code> 逻辑正确 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1240">#I3EHK7</a></li> 
 </ul> 
</blockquote> 
<h2 style="text-align:left">文档地址 </h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.blazor.zone%2F" target="_blank">https://www.blazor.zone/</a> </p> 
<h2 style="text-align:left">项目地址 </h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
</ul> 
<p style="text-align:left"><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">BootstrapBlazor</a><span style="background-color:#ffffff; color:#333333"> 遵循 </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/dev/LICENSE">Apache-2.0</a><span style="background-color:#ffffff; color:#333333"> 开源协议，欢迎大家提交 </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls?status=all">PR</a><span style="background-color:#ffffff; color:#333333"> 或 </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues?state=all">Issue</a><span style="background-color:#ffffff; color:#333333">。喜欢可以给个 </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">Star</a><span style="background-color:#ffffff; color:#333333">。</span> </p>
                                        </div>
                                      
</div>
            