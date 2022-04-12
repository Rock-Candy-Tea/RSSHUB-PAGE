
---
title: 'Jpom v2.8.18 已经发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=458'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 14:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=458'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jpom v2.8.18 已经发布，Java 项目在线管理</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】SSH文件管理器中加入创建目录和文件的功能 （感谢 <a href="https://www.oschina.net/wxyShine">@wxyShine </a> <a href="https://gitee.com/dromara/Jpom/pulls/161" target="_blank">Gitee PR 161</a> ）</li> 
 <li>【server】新增禁用登录图形验证码配置属性 <code>jpom.disabledCaptcha</code> （感谢 <a href="https://www.oschina.net/tt2yui">@放学后的茶会 </a> <a href="https://gitee.com/dromara/Jpom/issues/I4GD0U" target="_blank">Gitee issues I4GD0U</a> ）</li> 
 <li>【agent】节点项目文件管理新增创建文件夹/文件功能 （感谢 <a href="https://www.oschina.net/eibons">@Eibons </a> <a href="https://gitee.com/dromara/Jpom/issues/I4ZFFH" target="_blank">Gitee issues I4ZFFH</a> ）</li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【server】本地构建命令、本地命令发布、ssh 发布支持加载仓库目录 <code>.env</code> 文件为环境变量 （感谢@z~）</li> 
 <li>【server】容器相关引用 maven 版本升级为 3.8.5</li> 
 <li>【server】容器构建 DSL 示例添加镜像地址说明 （感谢 <a href="https://www.oschina.net/wxyShine">@wxyShine </a> <a href="https://gitee.com/dromara/Jpom/pulls/160" target="_blank">Gitee PR 160</a> ）</li> 
 <li>【server】本地构建命令添加本次构建相关的默认变量（感谢@杨杰）</li> 
 <li>【server】优化 SHH 文件管理中文件上传,压缩包上传操作（感谢 <a href="https://www.oschina.net/wxyShine">@wxyShine </a> <a href="https://gitee.com/dromara/Jpom/pulls/161" target="_blank">Gitee PR 161</a> ）</li> 
 <li>【agent】批量获取项目状态新增缓存，避免部分环境获取项目状态超时（感谢<a href="https://www.oschina.net/qiqi6666">@奇奇 </a> ）</li> 
 <li>远程升级检查地址支持自定义配置，解决没有外网或者网络不同情况下自定义配置升级服务器</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.18">https://gitee.com/dromara/Jpom/releases/v2.8.18</a></p>
                                        </div>
                                      
</div>
            