
---
title: 'PolarisMesh 北极星 V1.11.3 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-21eb3c778cc86c7f2cc5db4a156c529bfa1.png'
author: 开源中国
comments: false
date: Tue, 20 Sep 2022 15:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-21eb3c778cc86c7f2cc5db4a156c529bfa1.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="text-align:justify"><span style="color:#333333">北极星：一个支持多语言、多框架的云原生服务发现和治理中心，提供高性能SDK和无侵入Sidecar两种接入方式。</span></p> 
 <h2 style="text-align:justify"><strong style="color:#4f81bd">版本信息</strong></h2> 
 <h3 style="text-align:justify"><strong style="color:#4f81bd">北极星服务端</strong></h3> 
 <p style="text-align:justify"><span style="color:#333333">Release 链接： </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Freleases%2Ftag%2Fv1.11.3" target="_blank"><u>https://github.com/polarismesh/polaris/releases/tag/v1.11.3</u></a></p> 
 <h3 style="text-align:justify"><strong style="color:#4f81bd">主要变化</strong></h3> 
 <p style="text-align:justify"><span style="color:#333333">在 v1.11.3 版本中，我们主要对北极星的限流功能进行了以下优化</span><span style="color:#333333">，方便用户更好的使用北极星的单机限流和分布式限流能力</span></p> 
 <ol start="1"> 
  <li> <p style="text-align:justify"><span style="color:#333333">将限流规则从服务信息中独立为单独的功能栏;</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">在匹配计算方式上，我们支持了精确、正则、不等于、包好、不包含五种计算方式，更贴合用户实际的使用场景;</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">在请求匹配规则上，我们进一步划分了请求标签 key 的类型，方便用户理解当前流量标签的取值位置，同时也能够方便各个微服务框架组件，根据规则信息，自动的从流量对应的位置获取流量标签信息，标签key类型主要如下:</span></p> </li> 
 </ol> 
 <ul> 
  <li> <p style="text-align:justify"><span style="color:#333333">请求头（header）</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">请求参数（query）</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">主调服务</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">主调IP</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">用户自定义参数</span></p> </li> 
 </ul> 
 <p style="text-align:justify"><img alt height="1036" src="https://oscimg.oschina.net/oscnet/up-21eb3c778cc86c7f2cc5db4a156c529bfa1.png" width="1555" referrerpolicy="no-referrer"></p> 
 <h3 style="text-align:justify"><strong style="color:#4f81bd">其他变化</strong></h3> 
 <ul> 
  <li> <p style="text-align:justify"><span style="color:#333333">在动态路由功能栏中新增对于测试环境路由的指导手册。</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">配置中心支持配置模版功能，用户可以通过模板快速生成相关配置，PR链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Fpull%2F526" target="_blank"><u>https://github.com/polarismesh/polaris/pull/526</u></a></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">服务端报错支持国际化，方便国内用户使用中对于错误信息的理解，PR链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Fpull%2F550" target="_blank"><u>https://github.com/polarismesh/polaris/pull/550</u></a></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">配置中心代码结构调整以及代码优化，PR链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Fpull%2F553" target="_blank"><u>https://github.com/polarismesh/polaris/pull/553</u></a></p> </li> 
 </ul> 
 <ul> 
  <li> <p style="text-align:justify"><span style="color:#333333">修复北极星单机版本，实例注册后没有做任何操作但是实例的修改时间会发生变化导致SDK不断接受到更新事件问题，PR链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Fpull%2F527" target="_blank"><u>https://github.com/polarismesh/polaris/pull/527</u></a></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">eureka协议中针对心跳上报错误码的兼容问题，PR链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Fpull%2F670" target="_blank"><u>https://github.com/polarismesh/polaris/pull/670</u></a></p> </li> 
 </ul> 
 <p style="text-align:left"> </p> 
 <h3 style="text-align:justify"><strong style="color:#4f81bd">北极控制台</strong></h3> 
 <p style="text-align:justify"><span style="color:#333333">Release 链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris-console%2Freleases%2Ftag%2Fv1.8.1" target="_blank"><u>https://github.com/polarismesh/polaris-console/releases/tag/v1.8.1</u></a><span style="color:#333333"> </span></p> 
 <h4 style="text-align:justify"><strong style="color:#4f81bd">版本信息</strong></h4> 
 <ul> 
  <li> <p style="text-align:justify"><span style="color:#333333">创建配置文件时，文件的格式自动从文件名中识别。</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">调整创建配置文件页面 Card body 的高度，尽可能充满整个浏览器。</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">优化服务实例新增/编辑表单。</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">修复前端删除熔断规则最后一条时没有触发熔断规则解绑。</span></p> </li> 
 </ul> 
 <h3 style="text-align:justify"><strong style="color:#4f81bd">北极星 K8s Controller</strong></h3> 
 <p style="text-align:justify"><span style="color:#333333">Release 链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris-controller%2Freleases%2Ftag%2Fv1.3.0" target="_blank"><u>https://github.com/polarismesh/polaris-controller/releases/tag/v1.3.0</u></a></p> 
 <h4 style="text-align:justify"><strong style="color:#4f81bd">版本信息</strong></h4> 
 <ol start="1"> 
  <li> <p style="text-align:justify"><span style="color:#333333">支持部署在 kubernetes v1.22+ 以上的版本以及 kubernetes v1.21 以下的版本</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">支持获取 mtls 开关，为 envoy 开启 mtls 能力（beta功能）</span></p> </li> 
 </ol> 
 <h2 style="text-align:justify"><strong style="color:#4f81bd">新贡献者</strong></h2> 
 <p style="text-align:justify"><span style="color:#333333">北极星 v1.11.3 的发布离不开社区的贡献，以下是在北极星 v1.11.3 版本中新增的社区贡献者（以下排名不分先后）</span></p> 
 <ul> 
  <li> <p style="text-align:justify"><span style="color:#333333">@mhcvs2</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@GuiyangZhao</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@shuiqingliu</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@mangoGoForward</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@jim-kirisame</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@cocotyty</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@lhiamgeek</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@danlingliu</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">@yidafu</span></p> </li> 
 </ul> 
 <h2 style="text-align:justify"><strong style="color:#4f81bd">升级步骤</strong></h2> 
 <p style="text-align:justify"><strong style="color:#333333">注意：升级步骤仅针对部署了北极星集群版本</strong></p> 
 <h4 style="text-align:justify"><strong style="color:#4f81bd">之前已经安装过北极星集群</strong></h4> 
 <p><strong style="color:#4f81bd">执行 SQL 升级动作</strong></p> 
 <ul> 
  <li> <p style="text-align:justify"><span style="color:#333333">登陆北极星的MySQL存储实例</span></p> </li> 
  <li> <p style="text-align:justify"><span style="color:#333333">执行以下 SQL 语句</span></p> </li> 
 </ul> 
 <p style="text-align:left"> </p> 
 <pre><code>USE `polaris_server`;

CREATE TABLE `config_file_template` (
    `id` bigint(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
    `name` varchar(128) COLLATE utf8_bin NOT NULL COMMENT '配置文件模板名称',
    `content` longtext COLLATE utf8_bin NOT NULL COMMENT '配置文件模板内容',
    `format` varchar(16) COLLATE utf8_bin DEFAULT 'text' COMMENT '模板文件格式',
    `comment` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT '模板描述信息',
    `flag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '软删除标记位',
    `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `create_by` varchar(32) COLLATE utf8_bin DEFAULT NULL COMMENT '创建人',
    `modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    `modify_by` varchar(32) COLLATE utf8_bin DEFAULT NULL COMMENT '最后更新人',
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_name` (`name`)
) ENGINE=InnoDB COMMENT='配置文件模板表';

INSERT INTO `config_file_template` (`id`,`name`,`content`,`format`,`comment`,`create_time`,`create_by`,`modify_time`,`modify_by`) VALUES (2,'spring-cloud-gateway-braining','&#123;\n    \"rules\":[\n        &#123;\n            \"conditions\":[\n                &#123;\n                    \"key\":\"$&#123;http.query.uid&#125;\",\n                    \"values\":[\n                        \"10000\"\n                    ],\n                    \"operation\":\"EQUALS\"\n                &#125;\n            ],\n            \"labels\":[\n                &#123;\n                    \"key\":\"env\",\n                    \"value\":\"green\"\n                &#125;\n            ]\n        &#125;\n    ]\n&#125;','json','Spring Cloud Gateway  染色规则','2022-08-18 10:54:46','polaris','2022-08-18 10:55:22','polaris');


ALTER TABLE `ratelimit_config` CHANGE `cluster_id` `name` varchar(64) NOT NULL;
ALTER TABLE `ratelimit_config` ADD COLUMN `disable` tinyint(4)  NOT NULL DEFAULT '0';
ALTER TABLE `ratelimit_config` ADD COLUMN `etime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE `ratelimit_config` ADD COLUMN `method` varchar(512)   NOT NULL;

</code></pre> 
 <p> </p> 
 <h2 style="text-align:justify"><strong style="color:#4f81bd">下载地址</strong></h2> 
 <ul> 
  <li> <p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Freleases%2Ftag%2Fv1.11.3" target="_blank"><span style="color:#4f81bd">Github Release v1.11.3</span></a><span style="color:#4f81bd">：</span><span style="color:#4f81bd">https://github.com/polarismesh/polaris/releases/tag/v1.11.3</span></p> </li> 
  <li> <p style="text-align:justify"><a href="https://gitee.com/polarismesh/polaris/releases/tag/v1.11.3"><span style="color:#4f81bd">Gitee Release v1.11.3</span></a><span style="color:#4f81bd">：</span><span style="color:#4f81bd">https://gitee.com/polarismesh/polaris/releases/tag/v1.11.3</span></p> </li> 
 </ul> 
 <p style="text-align:justify"> </p> 
 <p style="text-align:justify"><span style="color:#333333">欢迎大家使用体验、Star、Fork、Issue，也欢迎大家参与 PolarisMesh 开源共建！</span></p> 
 <p style="text-align:justify"><span style="color:#333333">仓库地址：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris" target="_blank"><u>https://github.com/polarismesh/polaris</u></a></p> 
 <p style="text-align:justify"><span style="color:#333333">项目文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpolarismesh.cn%2Fzh%2Fdoc%2F" target="_blank"><u>https://polarismesh.cn/zh/doc/</u></a><span style="color:#333333">北极星是什么/简介.html</span></p> 
 <p style="text-align:justify"><span style="color:#333333">往期发布：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpolarismesh%2Fpolaris%2Freleases" target="_blank"><u>https://github.com/polarismesh/polaris/releases</u></a></p> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            