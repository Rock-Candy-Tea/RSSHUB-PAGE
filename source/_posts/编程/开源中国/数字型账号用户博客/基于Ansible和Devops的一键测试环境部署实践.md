
---
title: '基于Ansible和Devops的一键测试环境部署实践'
categories: 
 - 编程
 - 开源中国
 - 数字型账号用户博客
headimg: 'https://www.oschina.net/img/hot3.png'
author: 开源中国
comments: false
date: 2021-03-25 00:37:07
thumbnail: 'https://www.oschina.net/img/hot3.png'
---

<div>   
<div class="content">
                                                                                                                    <div class="ad-wrap" style="margin-bottom: 8px;">
            <a data-traceid="blog_detail_above_text_link_1" data-tracepid="blog_detail_above_text_link" style="color:#A00; font-weight:bold;" href="https://e.cn.miaozhen.com/r/k=2226845&p=7qZiO&dx=__IPDX__&rt=2&pro=s&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&o=https://ascend.huawei.com/zh/#/ecosystem/all-wisdom?utm_campaign=%252004MHQHQ210KA01N&utm_medium=pm-display&utm_source=OSCHINA&source=pc_blog&utm_object=ai_NA&utm_content=ascend_wisdom_ad" target="_blank">昇腾众智计划火热上线！140个算子/模型等你来挑战！>>><img src="https://www.oschina.net/img/hot3.png" align="absmiddle" style="max-height: 32px;max-width: 32px;margin-top: -4px;" referrerpolicy="no-referrer"></a>
            </div>
                                                                                                    <p style="text-align:center"><img alt height="359" src="https://oscimg.oschina.net/oscnet/up-db5f4776508947156a5918d863187e0df83.JPEG" width="640" referrerpolicy="no-referrer"></p> 
<p><span><strong><span style="color:#888888">​转载本文需注明出处：微信公众号EAWorld，违者必究。</span></strong></span></p> 
<p>随着网络架构的不断升级和业务的复杂化，对产品多环境支持的要求越来越高。产品支持的数据库、应用服务器、中间件、操作系统等的多样化，使测试环境的组合越来越多，导致测试环境的部署难度不断增加。</p> 
<p>如何选择一个合适的工具，实现多样化环境部署的同时保证部署操作的易用性。下面分享一下我们基于Ansible和Devops实现的一键式测试环境部署的过程。</p> 
<p>Ansible是一款自动化运维工具，基于Python开发，集合了众多运维工具（Saltstack、puppet、chef等）的优点，实现了批量系统配置、批量程序部署、批量运行命令等功能。Ansible是基于模块工作，具有丰富的内置模块，同时也支持自定义模块开发 1。以下是对Ansible和其他常见运维工具的对比2 ：</p> 
<p><img alt height="327" src="https://oscimg.oschina.net/oscnet/up-bff7238720a9b6865b0543ebdf0e9127d4f.png" width="726" referrerpolicy="no-referrer"></p> 
<p>而ansible在自动化运维过程时具有如下优势：</p> 
<p><strong>1.基于模块运行，有丰富的内置模块支持<br> 2. 基于Python开发，方便二次开发<br> 3. 基于SSH 交互，被管机器不要安装 Agent<br> 4. 无Server，在任何安装ansible的机器上执行命令即可<br> 5. 脚本用YAML编写，易读和易维护</strong></p> 
<p>正因为ansible操作简单、易上手，功能丰富，已被很多公司纳入使用。</p> 
<p>Ansible主要有ad-hoc和playbook两种执行方式，Ansible Ad-hoc是一次性命令，适合执行单个、简单的任务，一次只调用一个模块执行，如执行：</p> 
<pre><code class="language-javascript">ansible  -m yum -a “name=net-tools state=present“ </code></pre> 
<p>即可完成通过yum方式在远程机器上安装net-tools；执行</p> 
<pre><code class="language-javascript">ansible  -m service -a “name=httpd state= started“ </code></pre> 
<p>可以在远程服务其上启动httpd服务，若服务已启动，在远程机器上不会发生任何改变。</p> 
<p>Ansible Playbook模式使用YAML格式定义操作，通过模块编排完成复杂的操作，以角色(role)为执行单位，一个role包含多个文件目录，不同目录放置不同作用的文件，一个简单的playbook脚本目录结构如下所示：</p> 
<pre><code class="language-javascript">.
├── group_vars
│   └── all.yml
├── install.yml
├── linux.inventory
├── roles
│   └── test
│       ├── defaults
│       │   └── main.yml
│       ├── files
│       │   └── update.sh
│       ├── handlers
│       │   └── main.yml
│       ├── tasks
│       │   └── main.yml
│       ├── templates
│       │   └── server.xml
│       └── vars
│           └── main.yml
└── windows.inventory</code></pre> 
<p>每个目录下放置文件的具体作用为：</p> 
<p><strong>files：</strong>存放copy模块或script模块调用的文件<br> <strong>templates：</strong>存放jinja2模板<br> <strong>tasks：</strong>目录包含一个main.yml文件,该角色执行入口<br> <strong>handlers： </strong>角色中触发条件时执行的动作<br> <strong>vars： </strong>定义此角色用到的变量<br> <strong>defaults：</strong>为当前角色设定默认变量</p> 
<p>Playbook模式在安装有ansible 的机器上执行如下命令即可：</p> 
<pre><code class="language-javascript">ansible-playbook -ilinux.inventory install.yml --extra-vars “host=192.168.1.1”</code></pre> 
<p><strong>-i: </strong>用来指定具体的host inventory文件，默认使用/etc/ansible/hosts文件里面定义的主机或分组<br> <strong>--extra-vars: </strong>通过命令行方式指定部署用到的参数，通过命令行指定的参数优先级高于脚本中定义的参数</p> 
<p>下面介绍几个ansible中常用的一些模块。</p> 
<p><strong>1.set_fact</strong></p> 
<p>set_fact模块主要用来在部署过程中修改和新增变量，设置的变量可以在后面的role中使用。如依赖mysql数据库时，可通过set_fact 设置db_driver_class、db_driver_jar、db_url等参数,避免在执行时传入复杂的参数，减少执行时参数定义的复杂度，如下所示通过set_fact设置mysql数据库的连接信息。</p> 
<pre><code class="language-javascript">- name: set driver version
  when: db_version|string == '5.7'
  set_fact:
    db_driver_name: mysql-connector-java-5.1.32.jar
    db_platform: "org.hibernate.dialect.MySQLDialect"

- name: Set ipv4 db_url and driver name
  when: use_net4|bool
  set_fact:
    db_url: "jdbc:mysql://&#123;&#123; db_ip &#125;&#125;:&#123;&#123; db_port &#125;&#125;/&#123;&#123; db_name &#125;&#125;"
    db_driver: "com.mysql.jdbc.Driver"</code></pre> 
<p><strong>2.with_items</strong></p> 
<p>with_items模块用来执行循环，可与include_vars配合完成配置文件修改等操作。</p> 
<pre><code class="language-javascript">- include_vars: "common_vars.yml"

- name: modify install.properties
  lineinfile:
    path: "&#123;&#123; user_dir &#125;&#125;/config/install.properties"
    regexp: "&#123;&#123; re_item.original &#125;&#125;"
    line: "&#123;&#123; re_item.replace &#125;&#125;"
  with_items: "&#123;&#123; deploy_var &#125;&#125;"
  loop_control:
    loop_var: re_item</code></pre> 
<p><strong>3.include_tasks\include_role:</strong></p> 
<p>include_tasks\include_role模块主要用来引用其他task或role文件，实现功能复用和动态加载。在实际部署中可将不同类型的关联操作定义在相同的task或role中，执行中根据参数动态加载，如windows和linux下模块定义不一样，将windows和linux下的操作定义在不同的task中，根据执行时传入的os_type去执行不同的操作。</p> 
<pre><code class="language-javascript">- include_tasks: "common/&#123;&#123;os_type&#125;&#125;/main.yml"

- include_tasks: "dbinfo/set-&#123;&#123;db_type|lower&#125;&#125;.yml"

- include_role: "name=&#123;&#123;product_type&#125;&#125;"</code></pre> 
<p><strong>4.template</strong></p> 
<p>template模块主要将本地文件推送到远端，并将文件中的变量定义替换为运行时变量值，实现可变的配置。在实际部署中可以通过template修改tomcat的默认监听端口</p> 
<pre><code class="language-javascript">- name: create dir 
  file:
    state: directory
    dest: "&#123;&#123; app_server_home &#125;&#125;/conf"

- name: change tomcat server port
  template:
    src: "tomcat/server-&#123;&#123; app_server_version &#125;&#125;.xml"
    dest: "&#123;&#123; app_server_home &#125;&#125;/conf/server.xml"</code></pre> 
<p><strong>5.wait_for</strong></p> 
<p>wait_for模块主要用来判断端口监听、文件内容等条件是否满足条件。在实际部署中可以通过端口去判断服务是否启动，或者通过文件中是否包含指定内容去判断是否继续下一步操作。</p> 
<pre><code class="language-javascript">- name: wait server start
  when: have_app_server_port
  wait_for: 
    state: started
    port: "&#123;&#123;app_server_port&#125;&#125;"
    timeout: 60

- name: wait install success
  wait_for:  
    path: "&#123;&#123; user_dir &#125;&#125;/logs/install.log"
    search_regex: "esb.* installed successfully"</code></pre> 
<p>工作量，增加脚本的复用性，我们将产品的部署过程分为了以下几个步骤：</p> 
<p><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-5bc7702d36a3e040497c612eb7c8b9ee499.png" width="1093" referrerpolicy="no-referrer"></p> 
<p><strong>1.设置参数</strong></p> 
<p>为了保证整个部署脚本的扩展性和对不同产品、不同版本的支持，在部署过程中会有很多值需要参数化。部署过程中用到的很多参数，有些是不易理解和记忆的，如jdbc url、drive class等，每次执行脚本的时候需要再去查；还有一些参数对某个产品某个版本是固定的，可以根据一两个值确定下来。设置参数这一步主要是为了解决这个问题，预定义好部署过程中的诸多参数，通过参数控制部署流程和操作。</p> 
<pre><code class="language-javascript">- include_vars: "vars/&#123;&#123;os_type&#125;&#125;/main.yml"

- include_vars: "vars/&#123;&#123; product_type &#125;&#125;/main.yml"

- when: install_var_file == ''
  include_vars: "vars/&#123;&#123; product_type &#125;&#125;/var-&#123;&#123; product_version| string|lower &#125;&#125;.yml"

- when: install_var_file != ''
  include_vars: "&#123;&#123; install_var_file &#125;&#125;"

- include_tasks: ./common/silentinstall.yml

- include_tasks: "&#123;&#123; product_type &#125;&#125;/setfactor.yml"

- include_tasks: "dbinfo/set-&#123;&#123; db_type | lower &#125;&#125;.yml"

- include_tasks: "dbinfo/set-url.yml"</code></pre> 
<p><strong>2.虚拟机设置</strong></p> 
<p>在测试过程中，为了保证测试环境的有效性，每次部署的基础依赖环境是要干净的。但有些基础环境的准备如有些应用服务器或中间件等的安装是比较耗时的。为了保证干净的基础依赖环境并尽量简化部署过程的前提下，我们利用了虚拟机的快照功能。对于一些复杂的依赖环境，提前安装好并生成虚拟机快照，在部署过程中通过恢复快照的方式来简化部署过程。</p> 
<pre><code class="language-javascript">- include_vars: defaults/main.yml

- name: manage vm snapshot
  vmware_guest_snapshot:
    hostname: "&#123;&#123; vsphere_hostname &#125;&#125;"
    username: "&#123;&#123; vsphere_username &#125;&#125;"
    password: "&#123;&#123; vsphere_password &#125;&#125;"
    datacenter: "&#123;&#123; vsphere_datacenter &#125;&#125;"
    validate_certs: "&#123;&#123; validate_certs &#125;&#125;"
    name: "&#123;&#123; vm_name &#125;&#125;"
    folder: "&#123;&#123; vm_folder &#125;&#125;"
    state: "revert"
    snapshot_name: "&#123;&#123; vm_snapshot_name &#125;&#125;"
  delegate_to: localhost
  register: revertstate</code></pre> 
<p><strong>3.清理环境</strong></p> 
<p>为了保证产品安装目录未被占用，产品监听的端口处于空闲状态，需要对目录和端口进行清理操作。在执行清理环境过程中，对与有停止、卸载脚本的产品，调用脚本进行清理；没有停止、卸载服务的使用系统命令进行清    理。对于不存在的目录进行删除操作时的错误忽略。</p> 
<pre><code class="language-javascript">- name: copy killport file
  when: have_port
  template:
    src: killport.sh
    dest: "&#123;&#123; user_dir &#125;&#125;//killport.sh"
    mode: 0755

- name: close &#123;&#123; deploy_type &#125;&#125; application
  when: have_port
  shell: bash killport.sh
  args:
    chdir: "&#123;&#123; user_dir &#125;&#125;/"
  ignore_errors: yes

- name: close &#123;&#123; deploy_type &#125;&#125; application
  when: not have_port
  shell:  bash &#123;&#123; stopFile &#125;&#125; 
  args:
    chdir: "&#123;&#123; user_dir &#125;&#125;/"
  ignore_errors: yes

 - name: close &#123;&#123; deploy_type &#125;&#125; application
   when: not have_port
   shell:  ps -ef |grep "&#123;&#123; user_dir &#125;&#125;/&#123;&#123; deploy_type &#125;&#125;" |grep -v grep |awk '&#123;print $2&#125;' |xargs kill -9 
   args:
   chdir: "&#123;&#123; user_dir &#125;&#125;/"
   ignore_errors: yes</code></pre> 
<p><strong>4.部署依赖</strong></p> 
<p>部署依赖主要进行产品部署前的准备工作，包括JDK的安装、tomcat 端口配置等。通过参数定义，进行指定版本JDK，应用服务器等依赖的安装，并可对不同产品进行自定义配置。对于JDK安装、应用服务配置等操作都封装为单独的role以便复用。</p> 
<pre><code class="language-javascript">- include_role: name=jdk

- when: need_app_server|bool 
   include_role: name=deployappserver</code></pre> 
<p><strong>5.部署</strong></p> 
<p>部署主要为执行产品部署操作，主要进行安装包的获取，配置文件的修改、部署等操作。在执行过程中根据product_type参数选择对应的产品role，同一产品不同产品版本在同一role下定义不同的task执行不同的操作。</p> 
<pre><code class="language-javascript"> - include_role: name=setfactor

 - when: revert_state|bool
   include_role: name=revertsnapshot

 - include_role: name=cleanenv
 - include_role: name=getpackage

 - include_role: name=jdk

 - when: need_app_server|bool 
   include_role: name=deployappserver
 - include_role: name=&#123;&#123; product_type &#125;&#125;

 - when: start_server|bool
   include_role: name=startserver</code></pre> 
<p>具体的部署过程根据product_type定义不同的操作，其中一个产品部署操作如下所示：</p> 
<pre><code class="language-javascript">- include_vars: "common_vars.yml"

- include_vars: "&#123;&#123;product_module|lower&#125;&#125;.yml"
- name: modify install.properties
  lineinfile:
    path: "&#123;&#123; user_dir &#125;&#125;/config/install.properties"
    regexp: "&#123;&#123; re_item.original &#125;&#125;"
    line: "&#123;&#123; re_item.replace &#125;&#125;"
  with_items: "&#123;&#123; deploy_var &#125;&#125;"
  loop_control:
    loop_var: re_item
- name: update "install.sh"
  lineinfile:
    dest: "&#123;&#123; user_dir &#125;&#125;/install.sh"
    regexp: "&#123;&#123; item.line &#125;&#125;"
    line: "&#123;&#123; item.insertafter &#125;&#125;"
  with_items:
    - &#123; line: "^export P_I_JAVA_HOME=", insertafter: "export P_I_JAVA_HOME=&#123;&#123; local_java_home &#125;&#125;" &#125;

- name: install product  
  shell: ./install.sh
  args:
    chdir: "&#123;&#123; user_dir &#125;&#125;/"

- name: wait install success
  wait_for:  
    path: "&#123;&#123; user_dir &#125;&#125;/logs/install.log"
    search_regex: "esb.* installed successfully"
    timeout: 60</code></pre> 
<p><strong>6.启动</strong></p> 
<p>部署完成后修改启动参数，并启动服务，并检查服务的启动状态。</p> 
<pre><code class="language-javascript">- name: copy start.sh file
  template:
    src: start.sh
    dest: "&#123;&#123; install_dir &#125;&#125;/start.sh"
    mode: 0755

- name: change vm options
  when: app_server_name | lower == 'jboss'
  lineinfile: 
    dest: "&#123;&#123; install_dir &#125;&#125;/startServer.sh"
    regexp: 'Display our environment'
    line: 'JAVA_OPTS="$JAVA_OPTS -Xms2G -Xmx2G"'

- name: start Server
  shell:  bash start.sh
  args: 
    chdir: "&#123;&#123; install_dir &#125;&#125;"

- name: wait server start
  when: have_app_server_port
  wait_for: timeout=60 port="&#123;&#123; app_server_port &#125;&#125;" state=started</code></pre> 
<p>以上六个部署过程实现了不同产品测试环境的快速部署。</p> 
<p>部署脚本编写完成了，该如何有效的去执行部署脚本。每个产品部署时的数据库信息、应用服务器相关参数有十几二十个，每次去查看脚本定义来确定这些参数对每个测试人员是不友好的。结合普元Devops产品的发布流水线功能，就可快速便捷的实现测试环境部署。</p> 
<p>首先通过在DevOps中定义发布流水线，将产品部署流程分为代码仓库拉取脚本、部署产品和发送邮件三部分。<br> <img alt height="458" src="https://oscimg.oschina.net/oscnet/up-2457f0b8409584f7ffc8342934d28d97cf5.png" width="656" referrerpolicy="no-referrer"></p> 
<p>对于部署过程中的参数，通过发布流水线的参数化功能实现。将需要修改的参数定义为入参，这样在执行发布的时候可根据实际需要修改参数值。<br> <img alt height="503" src="https://oscimg.oschina.net/oscnet/up-dc9d82c8d7b42c355bd1a4020e8107502a2.png" width="1165" referrerpolicy="no-referrer"></p> 
<p>对于具有明确有限个值的参数，可定义为枚举类型的参数，并可以映射为易读易理解的名称，devops中对枚举类型的参数提供下拉选择框，方便部署过程中进行参数修改。可通过multiSelect属性定义实现单选和多选。</p> 
<p><img alt height="515" src="https://oscimg.oschina.net/oscnet/up-5d14da161da91fbafdac435066c44a69d31.png" width="764" referrerpolicy="no-referrer"></p> 
<p><img alt height="419" src="https://oscimg.oschina.net/oscnet/up-2c90abc6cbeff7e454cb9b4b334ea4765d0.png" width="862" referrerpolicy="no-referrer"></p> 
<p>所有参数化完成后，利用devops中shell脚本执行功能调用ansible-playbook命令并将定义的参数通过extra-vars选项传递给ansible完成测试环境的部署。</p> 
<p><img alt height="550" src="https://oscimg.oschina.net/oscnet/up-7d28d19d689c0ca52322bb43f4978a1a007.png" width="956" referrerpolicy="no-referrer"></p> 
<p>定义的发布流水线既可以通过定时构建触发，定时构建触发时使用参数定义的默认值；也可以手动发布，手动发布时可以动态修改部署参数。这样就可以根据测试需求快速实现不同组合环境的部署。</p> 
<p><img alt height="558" src="https://oscimg.oschina.net/oscnet/up-2037808ed9e0ed771d5595d90565e7549ec.png" width="940" referrerpolicy="no-referrer"></p> 
<p>对于不同的测试环境组合，也可以定义多个发布任务。根据实际的环境规划，对不同的任务通过标签进行分类管理，就可以快速定位部署任务，也可以有效实现环境部署任务的管理。</p> 
<p><img alt height="463" src="https://oscimg.oschina.net/oscnet/up-63bea0cf22678ca02a0b5392f4d79d570f8.png" width="1731" referrerpolicy="no-referrer"></p> 
<p> Ansible结合Devops，既实现了多产品多组合环境的快速部署，也完成了对环境部署任务的高效管理，为产品测试过程中环境提供保障。</p> 
<p><span style="color:#888888">参考资料</span></p> 
<p><span style="color:#888888">1：https://baike.baidu.com/item/ansible/20194655?fr=aladdin</span></p> 
<p><span style="color:#888888">2：https://www.edureka.co/blog/chef-vs-puppet-vs-ansible-vs-saltstack/</span></p> 
<p> </p> 
<p><span style="background-color:#888888; color:#f8f8f9">  - end -  </span></p> 
<p><img align="left" alt height="175" src="https://oscimg.oschina.net/oscnet/up-e73b26f1730212c2bbec451c637a983818f.png" width="124" referrerpolicy="no-referrer"><span><strong>关于作者</strong><span>：</span></span>dozeno，高级测试开发工程师，主要参与EOS、ESB等产品的自动化测试和持续部署工作，热衷于自动化测试、持续部署和Devops等相关技术。</p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p><img align="left" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWaNBdc2NWGRMLOZT5ntKc9qSzg9vyORia2VmUhhfsXx4Q9xBBSFIPDEF7y4YKDpy1uG37WliaqCBbw/640?wx_fmt=png" width="130" referrerpolicy="no-referrer"><span><strong><span>关于EAWorld</span></strong><span>：微服务，DevOps，数据治理，移动架构原创技术分享。<strong>长按二维码关注！</strong></span></span></p> 
<p> </p>
                                        </div>
                                      
</div>
            