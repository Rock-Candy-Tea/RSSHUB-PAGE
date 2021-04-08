
---
title: 'Bootstrap Blazor 更新版本 5.0.24'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5851'
author: 开源中国
comments: false
date: Thu, 08 Apr 2021 14:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5851'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 80 个组件，欢迎大家尝试使用。</span></h4> 
<h4 style="text-align:start">增加功能</h4> 
<ul> 
 <li> <p>!1278 feat(#I3HT3D): <code>Upload</code> 组件支持内置到 <code>ValidateForm</code> 使用 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1278">#I3HT3D</a></p> 
  <ol> 
   <li>通过设置绑定模型 <code>FileValidation</code> 标签可进行文件 <strong>类型</strong> 与 <strong>大小</strong> 客户端验证</li> 
   <li>支持 <code>NET</code> 内置的验证组件如：<code>Required</code></li> 
  </ol> </li> 
 <li> <p>!1276 feat(#I3HK4J): <code>Table</code> 组件增加 <code>IsTree</code> 参数控制数据是否有树形结构 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1276">#I3HK4J</a></p> </li> 
 <li> <p>!1271 feat(#I3GOGP): <code>Display</code> 组件增加 <code>Data</code> 参数用于通过 <code>Value</code> 显示 <code>Text</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1271">#I3GOGP</a></p> 
  <ol> 
   <li>此功能为 <code>CheckboxList</code> 或者 <code>Select</code> 组件设计，由于绑定数据可能是数值，用于显示时需要显示 <code>Text</code> 值</li> 
  </ol> </li> 
 <li> <p>!1268 feat(#I3FKWM): <code>Display</code> 提供 <code>FormatterAsync</code> 回调委托 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1268">#I3FKWM</a></p> 
  <ol> 
   <li><code>Display</code> 组件提供 <code>FormatterAsync</code> 异步格式化回调委托方法方便 <code>wasm</code> 模式调用 <code>webapi</code> 使用</li> 
  </ol> </li> 
 <li> <p>!1263 feat(#I3F81W): 增加新组件 <code>Display</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1263">#I3F81W</a></p> 
  <ol> 
   <li>此组件支持双向绑定，与表单组件功能一致，但是无客户端验证，无法输入 <code>UI</code> 渲染为 <code>div</code></li> 
  </ol> </li> 
 <li> <p>!1262 feat(#I3F0V9): <code>Avatar</code> 组件增加 <code>GetUrlAsync</code> 回调委托方法用于异步获取图片地址 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1262">#I3F0V9</a></p> 
  <ol> 
   <li>此功能非常时候图片地址是由 <code>webapi</code> 等接口异步方式获取的场景</li> 
  </ol> </li> 
 <li> <p>!1261 feat(#I3EZMH): <code>Checkbox</code> 增加 <code>Color</code> 参数用于设置背景颜色 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1261">#I3EZMH</a></p> </li> 
 <li> <p>!1260 feat(#I3EZGY): <code>Select</code> 组件选项支持 <strong>禁用</strong> 功能 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1260">#I3EZGY</a></p> 
  <ol> 
   <li>通过设置 <code>SelectedItem</code> 的 <code>IsDisabled</code> 属性设置改候选项禁止被选中</li> 
  </ol> </li> 
 <li> <p>!1258 feat(#I3EX6X): 新增 <code>Title</code> 组件 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1258">#I3EX6X</a></p> 
  <ol> 
   <li>页面内通过 <Title Text="标题"></Title> 使用</li> 
   <li>使用注入服务</li> 
   <li>使用 <code>TitleService</code> 静态方法设置网页标题</li> 
  </ol> </li> 
</ul> 
<pre style="text-align:start"><code>[Inject]
[NotNull]
<strong>private</strong> TitleService? TitleService &#123; <strong>get</strong>; <strong>set</strong>; &#125;

<strong>protected</strong> <strong>override</strong> <strong>async</strong> Task <strong>OnAfterRenderAsync</strong>(<strong>bool</strong> firstRender)
&#123;
    <strong>await</strong> <strong>base</strong>.OnAfterRenderAsync(firstRender);

    <strong>await</strong> TitleService.SetTitle(<span style="color:#dd1144">"我是标题"</span>);
&#125;
</code></pre> 
<pre style="text-align:start"><code><strong>protected</strong> <strong>override</strong> <strong>async</strong> Task <strong>OnAfterRenderAsync</strong>(<strong>bool</strong> firstRender)
&#123;
    <strong>await</strong> <strong>base</strong>.OnAfterRenderAsync(firstRender);

    <strong>await</strong> TitleService.SetWebSiteTitle(<span style="color:#dd1144">"我是标题"</span>);
&#125;
</code></pre> 
<ul> 
 <li>!1248 feat(#I3EGFT): <code>TimePicker</code> 支持鼠标滚轮（适配 FireFox）<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1248">#I3EGFT</a></li> 
 <li>!1250 feat(#I3EPO5): <code>Toast</code> 组件增加全局配置 <code>ToastPlacement</code> 参数可全站统一设置 <code>Toast</code> 弹出窗位置 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1250">#I3EPO5</a></li> 
</ul> 
<h4 style="text-align:start">问题修复</h4> 
<ul> 
 <li> <p>!1280 fix(#I3HWSW): 修复 <code>LambdaExtensions</code> 静态方法 <code>GetPropertyValueLambda</code> 与 <code>SetPropertyValueLambda</code> 方法内部获取属性时报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1280">#I3HWSW</a></p> 
  <ol> 
   <li>当子类使用 <code>new</code> 关键字更改父类属性类型时复现此问题</li> 
  </ol> </li> 
 <li> <p>!1264 fix(#I3F9DM): 修复 <code>Upload</code> 组件更新为泛型后客户端验证一直失败问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1264">#I3F9DM</a></p> </li> 
 <li> <p>!1259 fix(#I3EY3W): 修复 <code>Table</code> 组件未使用 <code>SelectedRows</code> 双向绑定时，此值始终为 <code>null</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1259">#I3EY3W</a></p> </li> 
 <li> <p>!1257 fix(#I3EVJM): 修复 <code>Table</code> 组件页面每次弹出 <code>Dialog</code> 后导致网页中有残留 <code>div</code> 问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1257">#I3EVJM</a></p> 
  <ol> 
   <li>多次弹窗后导致页面内有多个弹窗元素残留</li> 
  </ol> </li> 
 <li> <p>!1251 fix(#I3EPOP): 修复 <code>Step</code> 组件特定情况下丢失 <code>Step</code> 标签问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1251">#I3EPOP</a></p> </li> 
 <li> <p>!1247 fix(#I3EPMB): <code>Table</code> 组件 <code>SearchText</code> 搜索条件拼装时使用 <code>Or</code> 逻辑 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1247">#I3EPMB</a></p> </li> 
 <li> <p>!1249 fix(#I3EPN1): <code>Table</code> 组件 移动端列可见功能不可用问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1249">#I3EPN1</a></p> </li> 
</ul> 
<h4 style="text-align:start">示例更新</h4> 
<ul> 
 <li>!1270 docs(#I3GLM6): 更新 <code>PopconfirmButton</code> <code>TableToolbarPopconfirmButton</code> 按钮默认值 
  <ol> 
   <li><code>Cancel</code> 对应 <strong>取消</strong> <code>Ok</code> 对应 <strong>确定</strong></li> 
  </ol> </li> 
 <li>!1262 docs(#I3F0V9): 更新 <code>Avatar</code> 异步获取图片地址示例</li> 
 <li>!1265 docs(#I3FA8Y): 更新 <code>Table</code> 组件单元格内使用 <code>PopConfirmButton</code> 示例</li> 
</ul> 
<h4 style="text-align:start">性能优化</h4> 
<ul> 
 <li> <p>!1272 perf(#I3H1FQ): 优化组件 <code>Dispose</code> 逻辑增加 <code>javascript</code> 脚本资源释放逻辑 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1272">#I3H1FQ</a></p> </li> 
 <li> <p>!1267 refactor(#I3FBXA): 移除 CultureStorageExtensions 扩展类 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1267">#I3FBXA</a></p> 
  <ol> 
   <li>使用内置 <code>OperatingSystem.IsBrowser()</code> 检测 <code>wasm</code></li> 
  </ol> </li> 
 <li> <p>!1266 refactor(#I3FBU8): <code>TableCellButton</code> 组件移除 <code>TItem</code> <code>Item</code> 两个参数，精简代码 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1266">#I3FBU8</a></p> 
  <ol> 
   <li>破坏性更新，<code>OnClickCallback</code> 回调委托方法写法更新如下</li> 
   <li>移除 <code>OnClickWithoutRenderCallback</code> 与 <code>OnClickWithoutRender</code> 合并</li> 
  </ol> </li> 
</ul> 
<pre style="text-align:start"><code><TableCellButton <span style="color:#008080">Size</span>=<span style="color:#dd1144">"Size.ExtraSmall"</span> <span style="color:#008080">Color</span>=<span style="color:#dd1144">"Color.Primary"</span> <span style="color:#008080">Icon</span>=<span style="color:#dd1144">"fa fa-edit"</span> <span style="color:#008080">Text</span>=<span style="color:#dd1144">"明细"</span> <span style="color:#008080">OnClickCallback</span>=<span style="color:#dd1144">"@(() => OnRowButtonClick(context))"</span> /></code>
</pre> 
<p style="text-align:left">更新历史 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/wikis/v5.0.24?sort_id=3857954">传送门</a></p> 
<h2 style="text-align:left">项目地址</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p>
                                        </div>
                                      
</div>
            