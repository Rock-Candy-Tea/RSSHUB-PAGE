
---
title: 'Diboot 2.2.1 发布，更高效易用的开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8432'
author: 开源中国
comments: false
date: Mon, 17 May 2021 14:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8432'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Diboot是为开发者所打造的一个低代码开发平台，一个数倍提效的赋能工具。</p> 
<p style="text-align:start">Diboot不但拥有从前端到后端的整个基础架构，帮你更快开展项目。而且还拥有开发过程中的前后端一系列已有组件，助你少造轮子。还具有一套自动化工具，在开发过程中，前后端方面都可以帮您提质增效。</p> 
<p style="text-align:start">Diboot将致力于有效提高软件的代码质量、开发效率、可维护性，同时也对其打造了自动化工具来完成系列重复工作和复杂工作。</p> 
<p style="text-align:start">Diboot将通过系列基础组件化繁为简，又通过高效工具以简驭繁。</p> 
<h3 style="text-align:start">更新内容</h3> 
<p><span style="background-color:#ffffff; color:#404040">在此版本中，我们主要新增了消息通知组件（diboot-message-starter），进行了BindQuery注解优化、core缓存优化、IAM权限配置优化等，升级了antd前端项目基础代码，更新了antd前端项目的富文本编辑器等。</span></p> 
<h4 style="text-align:start">diboot-core & diboot-core-starter</h4> 
<ul> 
 <li>🎉 新增： @BindQuery注解新增strategy参数，支持空值处理策略（默认忽略空字符串）</li> 
 <li>🎉 新增： 基于Spring的内存缓存实现（BaseCacheManager），并优化绑定缓存实现</li> 
 <li>🎉 新增： SqlFileInitializer新增executeMultipleUpdateSqlsWithTransaction，支持事务的多SQL更新</li> 
 <li>🎉 新增： BaseService新增IService的getMap(queryWrapper)等接口</li> 
 <li>🎉 新增： @CollectThisApi注解，自动提取注解对应的rest接口</li> 
 <li>🎉 新增： 工具类 S.splitToList，D.formatDurationLabel等</li> 
 <li>🍻 优化：关联绑定的实现中字段名列名的转换由规则转换改为精确转换</li> 
 <li>🍻 优化：支持BindField&BindDict组合使用</li> 
 <li>🍻 优化：BeanUtils.convertValueToFieldType支持LocalDateTime转换</li> 
 <li>BUG：修复@BindQuery查询不支持自定义逻辑删除字段的问题</li> 
 <li>升级依赖jar至最新(spring boot 2.4.5, mybatis-plus 3.4.2等)</li> 
</ul> 
<h4 style="text-align:start">diboot-iam-starter</h4> 
<ul> 
 <li>🎉 新增：权限纠错功能，支持上线前自动检查配置的错误接口</li> 
 <li>🎉 新增：IamOrgService新增getParentOrgIds接口，支持获取部门的上级ids</li> 
 <li>🍻 优化：@Log日志记录支持POST等非url参数</li> 
</ul> 
<h4 style="text-align:start">diboot-file-starter</h4> 
<ul> 
 <li>🎉 新增：静态方法excel文件流读取</li> 
 <li>🎉 新增：FileStorageService.upload(inputStream, fileName)接口</li> 
 <li>🍻 优化：最小粒度重写替换excel上传本地存储</li> 
</ul> 
<h4 style="text-align:start">diboot-message-starter</h4> 
<ul> 
 <li>🎉 Starter启动自动安装依赖的数据表</li> 
 <li>🎉 支持自定义扩展消息发送，默认实现mail提供简单邮件发送</li> 
 <li>🎉 支持@TemplateVariable注解实现自定义模版变量和自动提取</li> 
 <li>🎉 启用devtools，自动生成初始样例controller代码到本地</li> 
</ul> 
<h4 style="text-align:start">Devtools</h4> 
<ul> 
 <li>🎉 新增：对普通用户开放前端页面设计功能体验</li> 
 <li>🎉 新增：消息模块初始化代码生成</li> 
 <li>🍻 优化：cloud环境下支持生成模块下的CommonController</li> 
</ul> 
<h4 style="text-align:start">前端项目 diboot-antd-admin</h4> 
<ul> 
 <li>🎉 新增：消息模版功能</li> 
 <li>🎉 新增：消息发送记录功能</li> 
 <li>🎉 新增：权限纠错功能，上线前自动检查配置的错误接口</li> 
 <li>🎉 新增：上线注意事项</li> 
 <li>🎉 新增：tinymce富文本编辑器</li> 
 <li>🍻 优化：系列代码与依赖升级，与ant design pro3.0.1版本一致</li> 
 <li>🍻 优化：新建按钮权限配置，增加自定义权限code输入方式</li> 
 <li>🍻 优化: 文件上传图片显示大小一致</li> 
 <li>🍻 优化：权限配置页面添加“按钮”的操作交互更直观</li> 
</ul> 
<h4 style="text-align:start">前端项目 diboot-element-admin</h4> 
<ul> 
 <li>🎉 新增：消息模版功能</li> 
 <li>🎉 新增：消息发送记录功能</li> 
 <li>🎉 新增：权限纠错功能，上线前自动检查配置的错误接口</li> 
 <li>🎉 新增：上线注意事项</li> 
 <li>🍻 优化: 文件上传图片显示大小一致</li> 
 <li>🍻 优化：权限配置页面添加“按钮”的操作交互更直观</li> 
</ul> 
<h4 style="text-align:start">微服务项目 diboot-cloud</h4> 
<ul> 
 <li>🎉 新增：消息服务模块及管理功能</li> 
 <li>🎉 新增：dockerfile与docker镜像打包相关的maven配置</li> 
 <li>🎉 新增：公用字典DictionaryApiService新增getKeyValueList接口</li> 
 <li>🍻 优化：富文本组件</li> 
 <li>🍻 优化：@Log日志记录支持POST等非url参数</li> 
 <li>🍻 优化：BindJob注解替换为CollectThisJob</li> 
 <li>BUG: 修复前端下拉框数据初始化不支持调用当前服务下的attachMore的问题</li> 
 <li>升级依赖jar至最新(spring cloud Hoxton.SR11，spring boot 2.3.10等)</li> 
</ul>
                                        </div>
                                      
</div>
            