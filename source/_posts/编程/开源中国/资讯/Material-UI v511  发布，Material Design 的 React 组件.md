
---
title: 'Material-UI v5.1.1  发布，Material Design 的 React 组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1118/071521_7SI0_5430600.png'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 07:16:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1118/071521_7SI0_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">material-ui<span> </span><span style="color:#24292f">v5.1.1 发布了，这个版本主要变更是将<strong><span> </span></strong></span><code>@mui/core</code><span> </span>包重命名为<span> </span><code>@mui/base</code>，因为这个包的内容是<span style="color:#2e3033">作为构建基础的非样式组件、hooks 和实用程序，用“base”命名比较合适。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">除了这个包的命名变更，</span><span style="color:#24292f">v5.1.1<span> </span></span><span style="color:#2e3033">还包含一些优化、bug 修复和测试项更新：</span></p> 
<h2 style="margin-left:0.6em; margin-right:0px; text-align:start"><strong>@mui/material@5.1.1</strong></h2> 
<ul> 
 <li style="text-align:start"><span style="color:#2e3033">[breadcrumb][Divider]：将十进制的间距值换成整数和 css calc 。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29526" target="_blank">#29526</a><span> </span>) </li> 
 <li style="text-align:start"><span style="color:#24292f">[Select][NativeSelect]： 加入<span> </span></span><code>multiple</code><span style="color:#24292f"><span> </span>类 。 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29566" target="_blank">#29566</a><span style="color:#24292f">)</span></li> 
 <li style="text-align:start"><span style="color:#24292f">[Popper]：</span><span style="color:#2e3033">拆分成 PopperUnstyled 和 Popper。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29488" target="_blank">#29488</a><span> </span>) </li> 
 <li style="text-align:start"><span style="color:#24292f">​[Select]： 明确<span> </span></span><code>Select</code><span style="color:#24292f"><span> </span>不是根组件。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29593" target="_blank">#29593</a><span style="color:#24292f">)</span></li> 
 <li style="text-align:start"><span style="color:#24292f">​[l10n]：改进荷兰语 (nl-NL) 环境缺少的一些翻译。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29592" target="_blank">#29592</a><span style="color:#24292f">)</span></li> 
 <li style="text-align:start"><span style="color:#24292f">​[Table]：改进分页显示，用破折号代替连字符。</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29579" target="_blank">#29579</a>）（就是下面这种视觉效果 ↓ ）</li> 
</ul> 
<p><img alt height="317" src="https://static.oschina.net/uploads/space/2021/1118/071521_7SI0_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0.6em; margin-right:0px; text-align:start"><strong>@mui/lab@5.0.0-alpha.55</strong></h2> 
<ul> 
 <li style="color: rgb(0, 0, 0); margin-left: 0px; margin-right: 0px; text-align: start;"><span style="color:#24292f">​[LoadingButton]：开始和结束的文本变量的间距固定。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29194" target="_blank">#29194</a><span style="color:#24292f">)</span></li> 
 <li style="color: rgb(0, 0, 0); margin-left: 0px; margin-right: 0px; text-align: start;"><span style="color:#24292f">​[Masonry]：</span><span style="color:#2e3033">检查容器或子容器是否存在，防止出错。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29452" target="_blank">#29452</a><span style="color:#24292f">) </span></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>DOS</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[文档] 使用旧版 MUI 构建的正确捆绑器配置。 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29146" target="_blank">#29146</a>)</li> 
 <li>[文档] 修复 autocomplete.md 上的错字。 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29570" target="_blank">#</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetizer" target="_blank">29570</a>）</li> 
 <li>[文档] <span style="color:#2e3033">修复品牌页面的黑暗模式。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29611" target="_blank">#29611</a><span style="color:#24292f">)</span></li> 
 <li>[文档] 如果没有 CSS 类，则不在 API 文档导航栏中呈现 CSS 部分。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29622" target="_blank">#29622</a>）</li> 
 <li>[文档] 修复链接区域设置处理。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29624" target="_blank">#29624</a><span> </span>)</li> 
 <li>[文档] 修复搜索导航。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29623" target="_blank">#29623</a><span> </span>)</li> 
 <li>[文档] 修复失效链接，更新 MUI 包说明。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29583" target="_blank">#29583</a>）</li> 
 <li>[文档] 修复 Algolia 搜索 url 中重复的语言片段。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29483" target="_blank">#29483</a><span> </span>) </li> 
 <li>[文档] 更新<span> </span><code>ThemeProvider</code><span> </span>API 链接。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29573" target="_blank">#29573</a>）</li> 
 <li>[文档] 从支持页面删除 svg 图标。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29431" target="_blank">#29431</a><span> </span>) </li> 
 <li>[文档]<span> </span><span style="color:#2e3033">集成<span> </span></span><span style="color:#24292f">UXPin</span><span style="color:#2e3033"><span> </span>链接。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29422" target="_blank">#29422</a><span> </span>) </li> 
 <li>[文档] 链接到设计套件的新公共路线图。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29433" target="_blank">#29433</a><span> </span>)</li> 
 <li>[网站] 修复高级计划的发布日期。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29430" target="_blank">#29430</a><span> </span>) </li> 
 <li>[网站] 将 GitHub 图标按钮添加到导航栏。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29640" target="_blank">#29640</a><span> </span>)</li> 
 <li>[博客] 在 markdown 页面中支持多位作者。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29633" target="_blank">#<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fm4theushw" target="_blank">29633</a><span> </span>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Core</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[core] 添加<code>experiments</code>索引页。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29582" target="_blank">#<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsiriwatknp" target="_blank"><strong>29582</strong></a><span> </span>) </li> 
 <li>[core]  将 s3 存储桶所有权移至 mui-org。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29609" target="_blank">#29609</a><span> </span>) </li> 
 <li>[core] 改进支持请求消息。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29614" target="_blank">#29614</a><span> </span>) </li> 
 <li>[core] 使用支持请求 Github Action。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29594" target="_blank">#29594</a><span> </span>) </li> 
 <li>[core] 删除未使用的工具<span> </span><code>getJsxPreview</code><span> </span>。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29586" target="_blank">#29586</a><span> </span>) </li> 
 <li>[core] 使用 GitHub 问题表单。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F28038" target="_blank">#28038</a><span> </span>) </li> 
 <li>[core] 添加<span> </span><span style="color:#24292f">playground 。</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29423" target="_blank">#29423</a>）</li> 
 <li>[test] 正确识别<span> </span><code>raf</code><span> </span>助手的用途。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29683" target="_blank">#29683</a>）</li> 
 <li>[test] 验证是否如测试标题所示创建了一个 ImageList。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29565" target="_blank">#29565</a>）</li> 
 <li>[test] 替换<span> </span><code>createServerRender</code><span> </span>为<span> </span><code>createRenderer</code><span> </span>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29503" target="_blank">#29503</a>）</li> 
 <li>[test] 始终忽略“useLayoutEffect 对服务器没有影响”-警告。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29502" target="_blank">#29502</a>）</li> 
 <li>[test] 默认恢复 StrictMode。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29589" target="_blank">#29589</a><span> </span>) </li> 
 <li>[test] createPickerRender -> createPickerRenderer。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29575" target="_blank">#29575</a><span> </span>) </li> 
 <li>[test] 允许实验 CLI 运行精确测试。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29685" target="_blank">#29685</a><span> </span>) </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Freleases%2Ftag%2Fv5.1.1" target="_blank">https://github.com/mui-org/material-ui/releases/tag/v5.1.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            