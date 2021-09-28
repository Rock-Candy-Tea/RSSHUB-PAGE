
---
title: 'Java 开源办公开发平台 O2OA V6.3 发布 _ ElementUI 组件上线！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5b8e1ad859f64f8973efa239b23921eb64f.png'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 10:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5b8e1ad859f64f8973efa239b23921eb64f.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span>O2OA6.3<span>版本中，新增了一组基于</span>Vue<span>的</span>ElementUI<span>组件，在流程表单设计界面，就可以在左边的工具栏找到</span>ElementUI<span>组件。它能让界面设计更加简洁直观，只需要将对应的组件拖动到表单设计区域就可以创建组件，还能保证产品设计人员搭建逻辑清晰、搭建出结构合理且高效易用的产品。</span></span></span></p> 
<p style="text-align:center"><img height="359" src="https://oscimg.oschina.net/oscnet/up-5b8e1ad859f64f8973efa239b23921eb64f.png" width="275" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>创建界面的布局容器后，可以选择字段类型组件、自动完成框、计数器、选择框、级联选择器、按钮、通用组件等进行快速搭建，提升设计效率，让界面更加美观，结构更加合理。</span></span></span><span><span><span>以日期范围选择器为例，点击＂</span>Preview<span>＂按钮可预览组件样式：</span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"> </p> 
<p style="text-align:center"><img height="224" src="https://oscimg.oschina.net/oscnet/up-372b7391480ef0f2b904b05155f672ed250.png" width="296" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>保存表单就创建了一个用与选择日期范围的组件，组件的值会自动绑定到</span>“v-model”<span>属性指向的</span>key<span>，本例中，选择框的值被绑定到了</span>this.data.value1<span>中。</span></span></span><span><span><span>我们再给日期选择框添加一些快捷选项，保存表单后即可看到效果:</span></span></span></p> 
<p style="text-align:center"><img height="253" src="https://oscimg.oschina.net/oscnet/up-342d83a362aab1c61fd7a1d429de61bf001.png" width="417" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>除此之外，此次版本在流程管理中新增了</span>onlyoffice<span>控件、</span>wps<span>控件、金格控件、永中控件作为正文控件，支持在线编辑</span>word<span>、</span>excel<span>、</span>ppt<span>、</span>pdf<span>等文件，加强与同事之间的远程协同；新增了</span>LibreOffice<span>预览，满足了用户在线预览各类文件的需求，助力协同办公，实现高效的团队管理。</span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#262626">O2OA V6.3还包含其他的功能更新和问题修正，让平台更稳定，用户操作更方便：</span><span style="background-color:#ffffff; color:#333333"> </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">功能新增</p> 
<p>[通用]HTML编辑器CKEditor升级到4161，增加了阅读状态的图片延迟加载功能、浏览原图功能。涉及的应用有流程表单、内容管理表单和论坛帖子</p> 
<p>[数据中心]新增了查询视图中导出Excel的功能</p> 
<p>[内容管理]新增了内容管理文档的操作条中置顶的功能，并为内容管理列表增加置顶标记</p> 
<p>[服务管理]新增了服务管理的代理和接口开发界面调试的功能</p> 
<p>[流程管理]新增了表单设计界面增加数据模板的时候带入默认相关组件，数据模板导出字段配置自动获取的功能</p> 
<p>[流程管理]新增了onlyoffice控件</p> 
<p>[流程管理]新增了wps控件</p> 
<p>[流程管理]新增了金格控件</p> 
<p>[流程管理]新增了永中控件</p> 
<p>[流程管理]新增了LibreOffice预览</p> 
<p>[移动办公]新增了微信公众号，关注回复的消息的功能</p> 
<p>[移动办公]新增了企业微信考勤数据导入查询功能</p> 
<p>[移动办公]新增了移动端App支持tokenName修改的功能</p> 
<p>[移动办公]新增了移动端App支持通讯录权限控制的功能</p> 
<p>[移动办公]新增了移动端App个人信息页面的个人属性展现的功能</p> 
<p>[数据库]新增了南大通用GBASE华库数据库支持</p> 
<p>[日志]新增了服务器http request access log</p> 
<p>[流程平台]新增了流程起草权限增加群组设置的功能</p> 
<p>[内容管理]新增了根据条件查找附件的接口</p> 
<p>[流程平台]新增了流程起草增加权限校验</p> 
<p>[人员组织]新增了人员组织管理模块接口mockput和mockdelete</p> 
<p>[流程平台]新增了待办、待阅根据title查询</p> 
<p>[平台架构]新增了平台审计日志自定义程序分析功能</p> 
<p>[流程平台]增加了公文编辑器转换Word后加密的功能</p> 
<p>[流程平台]增加了公文编辑器加盖图片章的功能</p> 
<p>[流程平台]新增了公文编辑器增加标题字体定义的功能</p> 
<p>[流程平台]新增了公文编辑器保证版记在偶数页的功能</p> 
<p>[流程平台]新增了公文编辑器增加附件内容编辑的功能</p> 
<p>[流程平台]新增了公文编辑器增加编辑器属性配置的功能</p> 
<p>[平台架构]新增了主菜单排序设置功能，管理员可设置默认和强制方式</p> 
<p>[平台架构]新增了一组ElementUI组件</p> 
<p><span style="background-color:#ffffff; color:#333333">功能优化</span></p> 
<p>[考勤管理]优化了考勤管理界面</p> 
<p>[脚本API]优化了脚本API（增加了后台脚本API,增加了发送待阅、添加参阅）</p> 
<p>[内容管理]优化了内容管理表单事件，增加postSave、 postPublish</p> 
<p>[内容管理]整理了内容管理操作条的图标</p> 
<p>[移动办公]优化了主题切换功能</p> 
<p>[移动办公]优化了移动端已阅意见功能支持</p> 
<p>[移动办公]O2云连接配置UI修改，以及一些页面功能调整优化</p> 
<p>[移动办公]优化了移动端App分享功能</p> 
<p>[移动办公]优化了移动端App拍照功能</p> 
<p>[服务器]集群增加健康检查</p> 
<p>[服务器]优化了线程池</p> 
<p>[服务器]优化了缓存机制</p> 
<p>[认证]验证码改为全匹配,并更新验证码实现</p> 
<p>[内容管理]优化了文档发布消息发送条件，未配置消息类型不往消息处理器发送消息</p> 
<p>[人员组织]优化了人员身份唯一编码，使其根据组织编码和人员唯一编码生成</p> 
<p>[内容管理]优化了文档权限刷新，增加多线程处理，增加根据文档类型刷新权限</p> 
<p>[内容管理]优化了分页查询的查询速度</p> 
<p>[内容管理]优化了review表索引，减少不必要索引，增加联合索引</p> 
<p>[流程平台]优化了公文编辑器格式展现</p> 
<p>[流程平台]公文编辑器粘贴表格时，控制合适的宽度</p> 
<p>[流程平台]公文编辑器只有一个附件时不显示序号</p> 
<p>[平台架构]修复this.data绑定的Array数据类型问题</p> 
<p>[平台优化]基于Authorization请求头的系统认证</p> 
<p><span style="background-color:#ffffff; color:#333333">问题修复</span></p> 
<p>[流程管理]修复了重置处理人未剔除待办人的问题</p> 
<p>[流程管理]修复了人员选择保存范围刷新后变回精简的问题</p> 
<p>[内容管理]修复了内容管理设计端语言包上的一些问题</p> 
<p>[流程管理]修复了表单Tab组件设置宽度无效的问题</p> 
<p>[流程管理]修复了表单中TextArea组件只读时setData的问题</p> 
<p>[流程管理]修复了数据表格移动端条目为0时无添加按钮的问题</p> 
<p>[移动办公]修复了钉钉、企业微信考勤数据展现的bug</p> 
<p>[流程引擎]修复了定时节点无法清空已选值的bug</p> 
<p>[内容管理]修复了文档阅读记录出现cipher用户的问题</p> 
<p>[内容管理]修复了根据创建时间查询文档错误的问题</p> 
<p>[流程平台]修复了根据状态分页查找work的bug</p> 
<p>[内容管理]修复了文档保存时未保存置顶信息的问题</p> 
<p>[流程平台]修复了执行this.data.save脚本时，在表单未载入完全时，可能造成数据丢失的问题</p> 
<p>[平台架构]修复了loadCss方法会多次载入的问题</p> 
<p>[流程平台]去除流程启动前和流程结束前两个事件</p> 
<p>[平台架构]修复Promise的uncatch错误</p>
                                        </div>
                                      
</div>
            