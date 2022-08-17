
---
title: 'Laravel 9.25 发布，经典 PHP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5427'
author: 开源中国
comments: false
date: Wed, 17 Aug 2022 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5427'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">经典 PHP 框架 Laravel 现已更新到 9.25 版本，带来以下更新：</p> 
<h3><strong>添加</strong></h3> 
<ul> 
 <li>添加 whenNotExactly 到 Stringable ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43700" target="_blank">#43700</a> )</li> 
 <li>为 Model::query()->touch() 添加了批量更新时间戳的功能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43665" target="_blank">#43665</a> )</li> 
</ul> 
<h3><strong>修复</strong></h3> 
<ul> 
 <li>使用不受支持的列时，防止 db/model 命令出错 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43635" target="_blank">#43635</a> )</li> 
 <li>修复 ensureDependenciesExist 运行时错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43626" target="_blank">#43626</a> )</li> 
 <li>在 php 8.1 中自动转换字段的 Null 值导致的贬损警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43706" target="_blank">( #43706</a> )</li> 
 <li>db:table 命令正确处理不存在的表 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43669" target="_blank">#43669</a> )</li> 
</ul> 
<h3><strong>改变了</strong></h3> 
<ul> 
 <li>在 db 命令中处理关联模式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43636" target="_blank">#43636</a> )</li> 
 <li>允许在数组和模型上使用 chunkById ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43666" target="_blank">#43666</a> )</li> 
 <li>允许 int 值参数到 whereMonth() 和 whereDay() ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43668" target="_blank">#43668</a> )</li> 
 <li>清理旧的 if-else 语句 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43712" target="_blank">#43712</a> )</li> 
 <li>对 css 资产使用正确的“完整性”值 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F43714" target="_blank">#43714</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv9.25.0" target="_blank">https://github.com/laravel/framework/releases/tag/v9.25.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            