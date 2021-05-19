
---
title: 'Swagger 接口文档查看工具 uniadmin-apidoc 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://vkceyugu.cdn.bspapp.com/VKCEYUGU-f12e1180-fce8-465f-a4cd-9f2da88ca0e6/f5a65bef-756e-4e93-83ee-d47e176976a8.png'
author: 开源中国
comments: false
date: Tue, 18 May 2021 19:02:00 GMT
thumbnail: 'https://vkceyugu.cdn.bspapp.com/VKCEYUGU-f12e1180-fce8-465f-a4cd-9f2da88ca0e6/f5a65bef-756e-4e93-83ee-d47e176976a8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">uniadmin-apidoc是无侵入的Swagger3/OpenApi3.0接口文档查看工具UI。引用即可生效，无需自己配置路由，无需自己部署swagger-ui到public目录。 插件为你做好了一切，基于ThinkPHP6的无侵入OpenApi UI界面，基于swagger-bootstrap-ui制作。</p> 
<p style="text-align:start"><img alt="uniadmin" src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-f12e1180-fce8-465f-a4cd-9f2da88ca0e6/f5a65bef-756e-4e93-83ee-d47e176976a8.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:start">软件架构</h4> 
<p style="text-align:start">基于ThinPHP6的ServiceProvider与Swagger-Bootstrap-UI，适合所有thinkphp6.0项目。</p> 
<h4 style="text-align:start">安装教程</h4> 
<pre style="text-align:start"><code>composer require-dev zircote/swagger-php
composer require-dev uniadmin/uniadmin-apidoc dev-master
</code></pre> 
<h3 style="text-align:start">写一个文档</h3> 
<p style="text-align:start">在一个控制器比如app/controller/User.php里写一个标准的接开文档如下</p> 
<pre style="text-align:start"><code>/**
 * 用户登录
 * 
 * @OA\POST(
 *     tags=&#123;"核心模块"&#125;,
 *     summary="用户登录",
 *     description="支持账号密码、手机号、邮箱登录",
 *     path="/core/user/login",
 *     @OA\Response(response="200",description="获取成功"),
 *     @OA\Parameter(
 *       name="account",in="query",required=true,description="用户名",
 *       @OA\Schema(type="string")
 *     ),
 *     @OA\Parameter(
 *       name="password",in="query",required=true,description="用户密码",
 *       @OA\Schema(type="string")
 *     )
 * )
 *
 * @param  \think\Request  $request
 * @return \think\Response
 * @author jry <ijry@qq.com>
 */
public function login(Request $request)
&#123;
&#125;
</code></pre> 
<h4 style="text-align:start">使用说明</h4> 
<p style="text-align:start">访问 &#123;域名:端口&#125;/doc</p>
                                        </div>
                                      
</div>
            