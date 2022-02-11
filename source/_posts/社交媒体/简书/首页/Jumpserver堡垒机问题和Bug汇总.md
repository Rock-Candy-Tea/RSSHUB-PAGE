
---
title: 'Jumpserver堡垒机问题和Bug汇总'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<blockquote>
<p>欢迎关注个人公众号 DailyJobOps</p>
</blockquote>
<p>源站地址 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FaoJewECME5pr6vFdcMlIYg" target="_blank">Jumpserver堡垒机问题和Bug汇总</a></p>
<h2>背景</h2>
<p>最近在使用堡垒机过程中发现几个问题，这里做个汇总，希望能对大家有所帮助</p>
<p>问题1、<code>账号不存在</code>，提示”您输入的用户名或者密码不对，请重新输入“，最终错误次数超限，<code>被”锁定“</code></p>
<p>问题2、配置了”<code>动态用户名</code>（用户名是动态的，登录资产时使用当前用户的用户名登录）“ 会 <code>覆盖主机上同名的SA账号</code>（具有sudo高权限的管理账号）<code>即使从授权中取消该动态用户权限配置</code></p>
<p>问题3、celery task状态刷新一会online一会offline，导致<code>资产推送系统用户的时候卡死</code>问题</p>
<p>接下来我们一次描述和解答</p>
<h2>不存在的账号被<code>锁定</code>
</h2>
<blockquote>
<p>出现的问题是因为运维给开发人员开通账号的时候名字写错，比如开发叫 <code>betty1210</code>，结果运维失误导致告诉开发人员你的账号是<code>betty1211</code>，然后开发人员就开始了艰难的登录之旅</p>
</blockquote>
<h3>问题发现之旅</h3>
<p>1、后台存在账号 <code>betty1210</code> ，开发使用 <code>betty1211</code> 频繁登录被锁定<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="986" data-height="842"><img data-original-src="//upload-images.jianshu.io/upload_images/1394001-1c8adb78f1415818" data-original-width="986" data-original-height="842" data-original-format="image/png" data-original-filesize="197118" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在这里插入图片描述</div>
</div><p></p>
<p>2、管理员登录后台发现，后台实际无 <code>betty1211</code> 用户，存在的是 <code>betty1210</code> 用户；也当然<code>有效用户 betty1210</code> 是<code>没有被锁定</code>的<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1500" data-height="390"><img data-original-src="//upload-images.jianshu.io/upload_images/1394001-4251ec16bead9803" data-original-width="1500" data-original-height="390" data-original-format="image/png" data-original-filesize="80780" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在这里插入图片描述</div>
</div><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1500" data-height="563"><img data-original-src="//upload-images.jianshu.io/upload_images/1394001-931f6a8725266720" data-original-width="1500" data-original-height="563" data-original-format="image/png" data-original-filesize="157636" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在这里插入图片描述</div>
</div><br>
3、然后尝试把 <code>正确用户 betty1210</code> 修改为 <code>错误用户betty1211</code> ，发现 用户 betty1211 <code>被锁定</code><p></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1500" data-height="529"><img data-original-src="//upload-images.jianshu.io/upload_images/1394001-af2d9871249a6d8b" data-original-width="1500" data-original-height="529" data-original-format="image/png" data-original-filesize="164771" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在这里插入图片描述</div>
</div>
<h3>问题总结</h3>
<p>个人觉得一般遇到这种问题，大家普通的都会认定是密码不对，然后复制不行，就水写一个个打上去等等尝试，但是账号如果不存在直接提示说<code>该用户不存在</code> 多友好，也不用在怀疑自己密码那些输错了，各种尝试... ...</p>
<p>所以各位在设计用户模块的可以站在用户的角度思考下。</p>
<hr>
<h2>动态用户Bug</h2>
<blockquote>
<p>这个真的是个<code>Bug</code></p>
</blockquote>
<h3>背景</h3>
<p>起初公司内部是通过ansible批量管理系统，ansible会给管理员推送SA权限的个人账号，方便管理同时也做好审计日志记录是哪个管理员做的操作</p>
<p>在测试Jumpserver堡垒机的<code>动态用户</code>的时候给管理员James（假设这里管理员叫James）也分配了该<code>系统用户</code>。</p>
<p>注意：动态用户时系统用户的一个类别</p>
<p>之后测试通过之后管理员取消了该动态用户的权限授权，在之后通过镜像（为了方便，特殊SA账号集成到了镜像中）创建新的主机之后发现James账号的SA权限丢失。</p>
<p>-----> 咋就丢了呢？</p>
<p>1、通过分析主机的passwd 和 group 分析发现时间是在主机创建之后，Jumpserver同步系统账号的时间吻合，怀疑是Jumpserver导致</p>
<p>2、创建测试账号<code>JamesTest</code>分配动态用户权限，然后再回收该权限</p>
<p>3、Jumpserver在测试主机上推送动态用户，发现还是会给该主机继续推送<code>JamesTest</code> 动态用户</p>
<p>也验证了确实是Jumpserver的问题导致</p>
<p>4、分析问题</p>
<p>由于篇幅问题，这里简化分析过程，<code>看大家的反馈，有必要的话会整理个更加详细的分析过程</code></p>
<ul>
<li>主要是通过浏览器发现在新增 资产授权的时候，调用 <code>api/v1/perms/asset-permissions/</code> 通过该接口定位到文件<code>perms/api/asset/asset_permission.py</code>
</li>
</ul>
<pre><code class="python">class AssetPermissionViewSet(OrgBulkModelViewSet):
    """
    资产授权列表的增删改查api
    """
    ... ...
    model = AssetPermission
    serializer_class = serializers.AssetPermissionSerializer
    ... ...
</code></pre>
<ul>
<li>注意到model AssetPermission中 system_users关联了assets.SystemUser，而且有个users_display属性</li>
</ul>
<pre><code class="python">class AssetPermission(BasePermission):
    ... ...
    system_users = models.ManyToManyField('assets.SystemUser', related_name='granted_by_permissions', verbose_name=_("System user"))
    ... ...
    def users_display(self):
        names = [user.username for user in self.users.all()]
        return names
</code></pre>
<ul>
<li>在 <code>perms/serializers/asset/permission.py</code> 文件中分析 <code>AssetPermissionViewSet</code> 中的<code>serializer_class</code> AssetPermissionSerializer 的 <code>perform_display_create</code> 中知道授权中涉及到的用户、用户组、资产、资产节点、系统用户都是通过这里进行创建的</li>
</ul>
<pre><code class="python">class AssetPermissionSerializer(BulkOrgResourceModelSerializer):
    ... ...
        def perform_display_create(self, instance, **kwargs):
        # 用户
        users_to_set = User.objects.filter(
            Q(name__in=kwargs.get('users_display')) | Q(username__in=kwargs.get('users_display'))
        ).distinct()
        instance.users.add(*users_to_set)
        # 用户组
        user_groups_to_set = UserGroup.objects.filter(name__in=kwargs.get('user_groups_display')).distinct()
        instance.user_groups.add(*user_groups_to_set)
        # 资产
        assets_to_set = Asset.objects.filter(
            Q(ip__in=kwargs.get('assets_display')) | Q(hostname__in=kwargs.get('assets_display'))
        ).distinct()
        instance.assets.add(*assets_to_set)
        # 节点
        nodes_to_set = Node.objects.filter(full_value__in=kwargs.get('nodes_display')).distinct()
        instance.nodes.add(*nodes_to_set)

    def create(self, validated_data):
        ... ...
        instance = super().create(validated_data)
        self.perform_display_create(instance, **display)
        return instance
</code></pre>
<ul>
<li><p>核心就是<code>instance.users.add</code>，通过之前的model关联关系，知道会把用户和它具有的系统用户报错在中间表 <code>assets_systemuser_users</code>中，</p></li>
<li><p>这里的create进行了perform重写，会写入相关表，但是delete做的时候没有做特殊处理，那么它就只会清理当前model对应的表，也就是<code>perms_assetpermission_users</code></p></li>
<li>
<p>然后在 <code>资产管理->系统用户->对应的动态用户</code> 打开进入到"资产列表中"点击主机后面的"<code>推送</code>"按钮 ，如下图所示，<br>
</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2874" data-height="1254"><img data-original-src="//upload-images.jianshu.io/upload_images/1394001-12489043fad39714" data-original-width="2874" data-original-height="1254" data-original-format="image/png" data-original-filesize="996387" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在这里插入图片描述</div>
</div>我们发现调用的接口是 <code>/api/v1/assets/system-users/261a5b51-b33a-4461-8c99-4c07c49cedae/tasks/</code>，主要涉及到 <code>SystemUserViewSet</code> 和 <code>SystemUser</code> model ，系统用户和用户的联系管理就保存在 表 <code>assets_systemuser_users</code> 中，而 授权清理的时候也没有清理这个表<p></p>
</li>
</ul>
<p>分析到这里，就知道授权清理存在Bug，只是删除了当前model对应的表数据，但是关联的 systemuser 而产生的中间表数据未清理</p>
<h3>解决</h3>
<p>知道对应的userid 和 systemuserid 从表  <code>assets_systemuser_users</code> 中清理相关数据，然后重新推送，发现推送记录中已经没有了JamesTest用户</p>
<hr>
<h2>Celery 僵死</h2>
<p>Celery的任务监控位于堡垒机 ”作业中心“下的”任务监控“ 中，点击打开新的页面如下图所示<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2876" data-height="734"><img data-original-src="//upload-images.jianshu.io/upload_images/1394001-33fdb398230500eb" data-original-width="2876" data-original-height="734" data-original-format="image/png" data-original-filesize="433730" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在这里插入图片描述</div>
</div><br>
刷新页面这里的status状态一会<code>Online</code>，一会又会<code>Offline</code>，如果尝试推送系统用户，那么遇到的页面的就是<code>**满屏幕的省略号**</code><p></p>
<p>主要的原因就是celery僵死导致</p>
<pre><code class="bash">[root@devops-jumpserver-vm ]# ps -A -ostat,ppid,pid,cmd |grep -e '^[Zz]'
Z+   26724 18914 [celery] <defunct>
Z+   26681 23138 [celery] <defunct>
</code></pre>
<p>尝试清理僵尸进程，发现导致jumpserver掉线，</p>
<pre><code class="bash">[root@devops-jumpserver-vm ]# kill -HUP `ps -A -ostat,ppid`|grep -e '^[Zz]'|awk '&#123;print $2&#125;'
Connection to devops-jumpserver-vm closed by remote host.
Connection to devops-jumpserver-vm closed.
</code></pre>
<p>这里需要注意📢：</p>
<p>堡垒机一般都是内网使用，如果一旦出现问题导致不可访问，那就是灾难性的，想登录堡垒机所在主机去排查修复都不可能了，所以一定要有一个备选方案，比如：<code>在堡垒机出现问题的时候可以通过临时绑定一个公网IP然后远程公网SSH登录去修复问题</code></p>
<p>登录Jumpserver尝试重启Jumpserver服务</p>
<pre><code class="bash"># status 发现堡垒机的状态都是 unhealthy 
[root@devops-jumpserver-vm ]# ./jmsctl.sh status
   Name                 Command                   State                           Ports
----------------------------------------------------------------------------------------------------------
jms_celery   ./entrypoint.sh start task       Up (unhealthy)   8070/tcp, 8080/tcp
jms_core     ./entrypoint.sh start web        Up (unhealthy)   8070/tcp, 8080/tcp
jms_koko     ./entrypoint.sh                  Up (unhealthy)   2222/tcp, 5000/tcp
jms_lion     /usr/bin/supervisord             Up (unhealthy)   4822/tcp
jms_nginx    /docker-entrypoint.sh ngin ...   Up (unhealthy)   0.0.0.0:22022->2222/tcp, 0.0.0.0:80->80/tcp
# 尝试重启
[root@devops-jumpserver-vm ]# ./jmsctl.sh restart
Stopping jms_core ... done
Stopping jms_koko ... done
Stopping jms_lion ... done
Stopping jms_nginx ... done
Stopping jms_celery ... done

jms_core is up-to-date
ERROR: for koko  Container "9f501157b5db" is unhealthy.
ERROR: for lion  Container "9f501157b5db" is unhealthy.
ERROR: for celery  Container "9f501157b5db" is unhealthy.
ERROR: for nginx  Container "9f501157b5db" is unhealthy.
ERROR: Encountered errors while bringing up the project.
</code></pre>
<p>重启失败，发现对应的容器也出现了<code>unhealthy</code>状态<br>
尝试重启docker</p>
<pre><code class="bash"># 重启docker
[root@devops-jumpserver-vm ]# systemctl restart docker

# 成功之后在重启Jumpserver
[root@devops-jumpserver-vm ]# ./jmsctl.sh restart
# 最后检查 Jumpserver的服务正常，访问恢复
[root@devops-jumpserver-vm ]# ./jmsctl.sh status
   Name                 Command                  State                          Ports
--------------------------------------------------------------------------------------------------------
jms_celery   ./entrypoint.sh start task       Up (healthy)   8070/tcp, 8080/tcp
jms_core     ./entrypoint.sh start web        Up (healthy)   8070/tcp, 8080/tcp
jms_koko     ./entrypoint.sh                  Up (healthy)   2222/tcp, 5000/tcp
jms_lion     /usr/bin/supervisord             Up (healthy)   4822/tcp
jms_nginx    /docker-entrypoint.sh ngin ...   Up (healthy)   0.0.0.0:22022->2222/tcp, 0.0.0.0:80->80/tcp
</code></pre>
<p>看到此处，欢迎点赞、转发，大家一起学习成长哦~</p>
<p>技术文章看累了，来个美图养养眼</p>
  
</div>
            