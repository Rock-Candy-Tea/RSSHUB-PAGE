
---
title: 'HertzBeat v1.0.beta.8 发布，易用友好的云监控系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/24788200/168501810-bd5ac38e-e2ea-473d-9418-80cac15f4745.png'
author: 开源中国
comments: false
date: Mon, 16 May 2022 09:28:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/24788200/168501810-bd5ac38e-e2ea-473d-9418-80cac15f4745.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat">HertzBeat 赫兹跳动</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>是由<span> </span></span><a href="https://gitee.com/link?target=https%3A%2F%2Fdromara.org">Dromara</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>孵化，</span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn">TanCloud</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>开源的一个支持网站，API，PING，端口，数据库，全站，操作系统等监控类型，支持</span><span style="background-color:#ffffff; color:#40485b">阈值告警，告警通知 (</span><span style="background-color:#efefef; color:#1c1e21">邮箱，webhook，钉钉，企业微信，飞书机器人</span><span style="background-color:#ffffff; color:#40485b">)</span><span style="background-color:#ffffff; color:#6a737d">，拥有易用友好的可视化操作界面的开源监控告警项目。</span>   </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
<p>最新版本 v1.0-beat.8 已经发布，除了支持更多的监控类型比如elasticSearch,中间件zookeeper等，我们还带来了期待已久的标签分组，更好看的主题，告警通知标签级别等过滤，告警平台化支持第三方告警信息接入，告警触发支持同类告警静默(不再频繁发送相同告警)，自定义用户权限支持，接收人配置测试等，此版本也大大增强了国际化支持，更多特性功能体验发现哦！</p> 
<p>首先感谢 hertzbeat 贡献者们的辛苦付出，@wang1027-wqh @gcdd1993 @a25017012 @MaxKeyTop @tomsun28<br> 还有社区用户们的生产使用反馈，这次大部分特性都是根据用户的反馈建议收集优化的。</p> 
<p>版本特性：</p> 
<ol> 
 <li>前端context路径由 '/console' 改为 '/', 后端接口统一context `api` #79</li> 
 <li>feature: 告警模块i18n #82 contribute by @wang1027-wqh</li> 
 <li>[home]feature: 官网i18n支持 #94 #81</li> 
 <li>feature:支持自定义告警信息控制台链接 #93 contribute by @wang1027-wqh</li> 
 <li>[manager]feature: 支持 ubuntu linux 和 centos linux 监控</li> 
 <li>[monitor]feature: 支持用户权限设置, admin-user-guest #101</li> 
 <li>[manager]feature: 重构告警转发模块 #106 contribute by @gcdd1993</li> 
 <li>feat: [collector,manager]feature:I18N Support #wqh #107 contribute by @wang1027-wqh</li> 
 <li>feat: [manager]feature: 支持ElasticSearch cluster 监控 #110 contribute by @wang1027-wqh</li> 
 <li>[monitor]feature: 支持标签，告警通知标签和级别过滤，告警平台 #111 contribute by @a25017012 @yuye</li> 
 <li>feature: 支持中间件zookeeper监控 #114 contribute by @wang1027-wqh</li> 
 <li>[manager]feature: 支持通知人测试按钮 #117</li> 
 <li>[monitor]feature: 支持相同告警信息时间段静默l. #123</li> 
 <li>[manager,webapp]feature: support alert define appHierarchy i18n #124</li> 
 <li>新的主题 contribute by @MaxKeyTop</li> 
</ol> 
<p>BUG修复</p> 
<ol> 
 <li>[collector]bugfix: bugfix: 解决 oracle采集不支持gbk编码问题 #84</li> 
 <li>[script]bugfix: windows bat脚本编码问题… #89</li> 
 <li>[web-app]bugfix: 告警中心过滤条件在分页时不生效问题</li> 
 <li>fix #96，TDengine时区错误 #98 contribute by @gcdd1993</li> 
 <li>[web-app]bugfix: dashboard加载告警信息异常问题 #105 contribute by @gcdd1993</li> 
 <li>[collector]bugfix: expression evaluation error when value with spaces #113</li> 
 <li>[manager,webapp]bugfix: 重复标签异常 #116</li> 
 <li>[manager]bugfix: linux.cpu.interrupt 指标采集错误问题 #118</li> 
 <li>[alerter]bugfix nextEvalInterval npe</li> 
 <li>通知异常问题修复 contribute by @MaxKeyTop</li> 
</ol> 
<p>⚠️⚠️⚠️ 版本升级注意：</p> 
<p>⚠️⚠️⚠️ 此版本 application.yml 和 sureness.yml 配置有改动，若之前对配置文件有更改，请在最新的配置文件基础上再次修改配置</p> 
<p>⚠️⚠️⚠️ 默认账户密码为 admin/hertzbeat , 可通过配置sureness.yml修改</p> 
<p>⚠️⚠️⚠️ v1.0-beat7 升级到最新 v1.0-beat8 需MYSQL数据库执行以下升级SQL:</p> 
<pre><code>use hertzbeat;

alter table alert add first_trigger_time bigint;
alter table alert add last_trigger_time bigint;
alter table alert add next_eval_interval bigint;
alter table alert add tags varchar(4000);
alter table alert add creator varchar(100);
alter table alert add modifier varchar(100);
alter table alert add gmt_update datetime;

alter table alert drop monitor_id;
alter table alert drop monitor_name;

alter table notice_rule add priorities varchar(100);
alter table notice_rule add tags varchar(4000);


-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS  tag ;
CREATE TABLE  tag
(
    id           bigint           not null auto_increment comment 'TAG ID',
    name         varchar(100)     not null comment 'TAG标签名称',
    value        varchar(100)     comment 'TAG标签值(可为空)',
    type         tinyint          not null default 0 comment '标记类型 0:监控自动生成(monitorId,monitorName) 1: 用户生成 2: 系统预制',
    color        varchar(100)     default '#ffffff' comment '标签颜色' ,
    creator      varchar(100)     comment '创建者',
    modifier     varchar(100)     comment '最新修改者',
    gmt_create   timestamp        default current_timestamp comment 'create time',
    gmt_update   datetime         default current_timestamp on update current_timestamp comment 'update time',
    primary key (id),
    unique key unique_tag (name, value)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for tag_monitor_bind
-- ----------------------------
DROP TABLE IF EXISTS  tag_monitor_bind ;
CREATE TABLE  tag_monitor_bind
(
    id           bigint           not null auto_increment comment '主键ID',
    tag_id       bigint           not null comment 'TAG ID',
    monitor_id   bigint           not null comment '监控ID',
    gmt_create   timestamp        default current_timestamp comment 'create time',
    gmt_update   datetime         default current_timestamp on update current_timestamp comment 'update time',
    primary key (id),
    index index_tag_monitor (tag_id, monitor_id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

</code></pre> 
<p>欢迎在线试用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a>.</p> 
<hr> 
<p>新增特性效果展示：<br> <img alt="截屏2022-05-16 08 37 48" src="https://user-images.githubusercontent.com/24788200/168501810-bd5ac38e-e2ea-473d-9418-80cac15f4745.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt="671652661240_ pic" src="https://user-images.githubusercontent.com/24788200/168501675-5291ad1a-aff3-4274-bbc8-8d2730862dc6.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt="681652661252_ pic" src="https://user-images.githubusercontent.com/24788200/168501708-3e24e7e5-0983-48b0-b25c-d8f691fe1793.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt="691652661259_ pic" src="https://user-images.githubusercontent.com/24788200/168501688-abda3488-8f54-433c-9078-9d04abbf6690.jpg" referrerpolicy="no-referrer"> <img alt="截屏2022-05-16 08 37 21" src="https://user-images.githubusercontent.com/24788200/168501827-bb604cf8-2c72-4cc5-990d-4d4e41db5e6e.png" width="781" referrerpolicy="no-referrer"></p> 
<p><img alt="截屏2022-05-16 08 37 00" src="https://user-images.githubusercontent.com/24788200/168501873-5caa8a26-13f3-445b-91f3-6aea26bd27de.png" width="773" referrerpolicy="no-referrer"> <img alt="截屏2022-05-16 08 36 45" src="https://user-images.githubusercontent.com/24788200/168501885-809bdf6d-f74f-45aa-a761-3022de2b8f69.png" width="1895" referrerpolicy="no-referrer"></p> 
<hr> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">HertzBeat赫兹跳动</a> 是一个支持网站，API，PING，端口，数据库，操作系统等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的 <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">SAAS版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">登录即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a> ,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code> 各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版，邮件钉钉微信飞书等及时通知送达<br> 欢迎登录 HertzBeat 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">云环境TanCloud</a> 试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
</blockquote> 
<blockquote> 
 <p><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
</blockquote> 
<p>老铁们可以通过演示视频来直观了解功能： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1DY4y1i7ts" target="_blank">https://www.bilibili.com/video/BV1DY4y1i7ts</a></p> 
<p>欢迎在线试用 <a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn">https://console.tancloud.cn</a></p> 
<p><strong>仓库地址</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">Github</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">https://github.com/dromara/hertzbeat</a><br> <a href="https://gitee.com/dromara/hertzbeat">Gitee</a> <a href="https://gitee.com/dromara/hertzbeat">https://gitee.com/dromara/hertzbeat</a></p> 
<p>看到这里不妨给个Star支持下哦，灰常感谢，弯腰!!</p>
                                        </div>
                                      
</div>
            