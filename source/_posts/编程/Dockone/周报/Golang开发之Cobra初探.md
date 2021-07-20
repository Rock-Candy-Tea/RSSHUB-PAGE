
---
title: 'Golang开发之Cobra初探'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9743'
author: Dockone
comments: false
date: 2021-07-20 05:06:04
thumbnail: 'https://picsum.photos/400/300?random=9743'
---

<div>   
<br>在云原生如日中天的当下，相信很多人对Kubernetes/etcd等都有所耳闻，当我们看其源码或对其进行二次开发的时候，可以发现其均使用了一个命令行程序库Cobra，其是一个用来编写命令行的神器，提供了一个脚手架，用于快速生成基于Cobra应用程序框架。<br>
<br><blockquote><br>其作者是非常有名的spf13，相信大家对Vim都有所了解，可以去使用Vim的终极终端spf13-vim，可以一键配置，非常的方便，其还有作品viper是一个完整的配置解决方案，支持JSON/YAML/TOML/HCL/envFile等配置文件，还可以热加载，配置保存等，hugo也是其的作品。</blockquote>我们可以利用Cobra快速的去开发出我们想要的命令行工具，非常的方便快捷。<br>
<h3>功能特性</h3><ul><li>简易的子命令行模式，如app server，app fetch等等</li><li>完全兼容posix命令行模式</li><li>嵌套子命令subcommand</li><li>支持全局，局部，串联flags</li><li>使用Cobra很容易的生成应用程序和命令，使用cobra create appname和cobra add cmdname</li><li>如果命令输入错误，将提供智能建议，如app srver，将提示srver没有，是否是app server</li><li>自动生成commands和flags的帮助信息</li><li>自动生成详细的help信息，如app help</li><li>自动识别-h，--help帮助flag</li><li>自动生成应用程序在bash下命令自动完成功能</li><li>自动生成应用程序的man手册</li><li>命令行别名</li><li>自定义help和usage信息</li><li>可选的紧密集成的viper apps</li></ul><br>
<br><h3>使用Cobra</h3><h4>安装</h4>Cobra安装非常简单，使用go get获取即可，安装完成后，打开GOPATH目录，bin目录下应该有已经编译好的Cobra，当然也可以使用源码编译安装。<br>
<br>在使用Cobra之前需要了解三个概念，其也是命令行的三部分内容：command、flag和args。<br>
<ul><li>命令自身的一些基本信息，用command表示，具体对象是：cobra.Command</li><li>命令的一些标致或者选项，用flag表示，具体对象是：flag.FlagSet</li><li>最后的参数，用args表示，通常是：[]string</li></ul><br>
<br>对应如下例子：<br>
<pre class="prettyprint">go get -u test.com/a/b<br>
</pre><br>
这里<code class="prettyprint">get</code>就是commond（这里比较特殊），<code class="prettyprint">-u</code>就是flag，<code class="prettyprint">test.com/a/b</code>就是args。<br>
<h4>生成应用程序</h4><pre class="prettyprint">$ /Users/xuel/workspace/goworkspace/bin/cobra init --pkg-name smartant-cli<br>
Your Cobra application is ready at<br>
/Users/xuel/workspace/goworkspace/src/github.com/kaliarch/smartant-cli<br>
$ ls<br>
LICENSE cmd     go.mod  go.sum  main.go<br>
$ tree<br>
.<br>
├── LICENSE<br>
├── cmd<br>
│   └── root.go<br>
├── go.mod<br>
├── go.sum<br>
└── main.go<br>
<br>
1 directory, 5 files<br>
</pre><br>
<h4>设计cls程序</h4>在smartant-cli目录下创建imp目录，器重编写utils.go文件，内入如下：<br>
<pre class="prettyprint">package utils<br>
<br>
import "fmt"<br>
<br>
func Show(name string, age int) &#123;<br>
fmt.Printf("name is %s, age is %d", name, age)<br>
&#125; <br>
</pre><br>
main.go：<br>
<pre class="prettyprint">package main<br>
<br>
import "github.com/kaliarch/smartant-cli/cmd"<br>
<br>
func main() &#123;<br>
cmd.Execute()<br>
&#125; <br>
</pre><br>
可以看出main函数执行cmd包，所以我们只需要在cmd包内调用utils包就能实现smartant-cli程序的需求。接着打开root.go文件查看：<br>
<br>root.go：<br>
<pre class="prettyprint">/*<br>
Copyright © 2021 NAME HERE <EMAIL ADDRESS><br>
<br>
Licensed under the Apache License, Version 2.0 (the "License");<br>
you may not use this file except in compliance with the License.<br>
You may obtain a copy of the License at<br>
<br>
http://www.apache.org/licenses/LICENSE-2.0<br>
<br>
Unless required by applicable law or agreed to in writing, software<br>
distributed under the License is distributed on an "AS IS" BASIS,<br>
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.<br>
See the License for the specific language governing permissions and<br>
limitations under the License.<br>
*/<br>
package cmd<br>
<br>
import (<br>
"fmt"<br>
"github.com/spf13/cobra"<br>
"os"<br>
<br>
homedir "github.com/mitchellh/go-homedir"<br>
"github.com/spf13/viper"<br>
)<br>
<br>
var cfgFile string<br>
<br>
// rootCmd represents the base command when called without any subcommands<br>
var rootCmd = &cobra.Command&#123;<br>
Use:   "smartant-cli",<br>
Short: "SmartAnt linux agent cli",<br>
Long: `<br>
smartant-cli is a CLI for SmartAnt applications.<br>
This application is a tool to migrations linux system.`,<br>
// Uncomment the following line if your bare application<br>
// has an action associated with it:<br>
//  Run: func(cmd *cobra.Command, args []string) &#123; &#125;,<br>
&#125;<br>
<br>
// Execute adds all child commands to the root command and sets flags appropriately.<br>
// This is called by main.main(). It only needs to happen once to the rootCmd.<br>
func Execute() &#123;<br>
if err := rootCmd.Execute(); err != nil &#123;<br>
    fmt.Println(err)<br>
    os.Exit(1)<br>
&#125;<br>
&#125;<br>
<br>
func init() &#123;<br>
cobra.OnInitialize(initConfig)<br>
<br>
// Here you will define your flags and configuration settings.<br>
// Cobra supports persistent flags, which, if defined here,<br>
// will be global for your application.<br>
<br>
rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.smartant-cli.yaml)")<br>
<br>
// Cobra also supports local flags, which will only run<br>
// when this action is called directly.<br>
rootCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")<br>
&#125;<br>
<br>
// initConfig reads in config file and ENV variables if set.<br>
func initConfig() &#123;<br>
if cfgFile != "" &#123;<br>
    // Use config file from the flag.<br>
    viper.SetConfigFile(cfgFile)<br>
&#125; else &#123;<br>
    // Find home directory.<br>
    home, err := homedir.Dir()<br>
    if err != nil &#123;<br>
        fmt.Println(err)<br>
        os.Exit(1)<br>
    &#125;<br>
<br>
    // Search config in home directory with name ".smartant-cli" (without extension).<br>
    viper.AddConfigPath(home)<br>
    viper.SetConfigName(".smartant-cli")<br>
&#125;<br>
<br>
viper.AutomaticEnv() // read in environment variables that match<br>
<br>
// If a config file is found, read it in.<br>
if err := viper.ReadInConfig(); err == nil &#123;<br>
    fmt.Println("Using config file:", viper.ConfigFileUsed())<br>
&#125;<br>
&#125; <br>
</pre><br>
从源代码来看cmd包进行了一些初始化操作并提供了Execute接口。十分简单，其中viper是cobra集成的配置文件读取的库，这里不需要使用，我们可以注释掉（不注释可能生成的应用程序很大约10M，这里没哟用到最好是注释掉）。cobra的所有命令都是通过cobra.Command这个结构体实现的。为了实现smartant-cli功能，显然我们需要修改RootCmd。修改后的代码如下：<br>
<pre class="prettyprint">/*<br>
Copyright © 2021 NAME HERE <EMAIL ADDRESS><br>
<br>
Licensed under the Apache License, Version 2.0 (the "License");<br>
you may not use this file except in compliance with the License.<br>
You may obtain a copy of the License at<br>
<br>
http://www.apache.org/licenses/LICENSE-2.0<br>
<br>
Unless required by applicable law or agreed to in writing, software<br>
distributed under the License is distributed on an "AS IS" BASIS,<br>
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.<br>
See the License for the specific language governing permissions and<br>
limitations under the License.<br>
*/<br>
package cmd<br>
<br>
import (<br>
"fmt"<br>
"github.com/spf13/cobra"<br>
//"github.com/spf13/viper"<br>
"github.com/kaliarch/cobra-demo/utils"<br>
"os"<br>
)<br>
<br>
var cfgFile string<br>
<br>
//var name string<br>
//var age int<br>
var command string<br>
<br>
// rootCmd represents the base command when called without any subcommands<br>
var rootCmd = &cobra.Command&#123;<br>
Use:   "cobra-demo",<br>
Short: "A brief description of your application",<br>
Long: `A longer description that spans multiple lines and likely contains<br>
examples and usage of using your application. For example:<br>
<br>
Cobra is a CLI library for Go that empowers applications.<br>
This application is a tool to generate the needed files<br>
to quickly create a Cobra application.`,<br>
// Uncomment the following line if your bare application<br>
// has an action associated with it:<br>
//  Run: func(cmd *cobra.Command, args []string) &#123; &#125;,<br>
Run: func(cmd *cobra.Command, args []string) &#123;<br>
    //if len(name) == 0 &#123;<br>
    //  cmd.Help()<br>
    //  return<br>
    //&#125;<br>
    //imp.Show(name, age)<br>
    if len(command) == 0 &#123;<br>
        cmd.Help()<br>
        return<br>
    &#125;<br>
    utils.Cmd(command)<br>
<br>
&#125;,<br>
&#125;<br>
<br>
// Execute adds all child commands to the root command and sets flags appropriately.<br>
// This is called by main.main(). It only needs to happen once to the rootCmd.<br>
func Execute() &#123;<br>
if err := rootCmd.Execute(); err != nil &#123;<br>
    fmt.Println(err)<br>
    os.Exit(-1)<br>
&#125;<br>
&#125;<br>
<br>
func init() &#123;<br>
//cobra.OnInitialize(initConfig)<br>
<br>
// Here you will define your flags and configuration settings.<br>
// Cobra supports persistent flags, which, if defined here,<br>
// will be global for your application.<br>
<br>
rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.smartant-agent.yaml)")<br>
<br>
// Cobra also supports local flags, which will only run<br>
// when this action is called directly.<br>
//rootCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")<br>
//rootCmd.PersistentFlags().StringVarP(&name, "name", "n", "", "person name")<br>
//rootCmd.PersistentFlags().IntVarP(&age, "age", "a", 0, "person age")<br>
rootCmd.PersistentFlags().StringVarP(&command, "command", "o", "", "execute command context")<br>
<br>
&#125;<br>
<br>
// initConfig reads in config file and ENV variables if set.<br>
//func initConfig() &#123;<br>
//  if cfgFile != "" &#123;<br>
//      // Use config file from the flag.<br>
//      viper.SetConfigFile(cfgFile)<br>
//  &#125; else &#123;<br>
//      // Find home directory.<br>
//      home, err := homedir.Dir()<br>
//      if err != nil &#123;<br>
//          fmt.Println(err)<br>
//          os.Exit(1)<br>
//      &#125;<br>
//<br>
//      // Search config in home directory with name ".cobra-demo" (without extension).<br>
//      viper.AddConfigPath(home)<br>
//      viper.SetConfigName(".cobra-demo")<br>
//  &#125;<br>
//<br>
//  viper.AutomaticEnv() // read in environment variables that match<br>
//<br>
//  // If a config file is found, read it in.<br>
//  if err := viper.ReadInConfig(); err == nil &#123;<br>
//      fmt.Println("Using config file:", viper.ConfigFileUsed())<br>
//  &#125;<br>
//&#125; <br>
</pre><br>
<h4>执行</h4><pre class="prettyprint"># 编译<br>
$ go build -o smartant-cli<br>
$ ./smartant-cli <br>
<br>
smartant-cli is a CLI for SmartAnt applications.<br>
This application is a tool to migrations linux system.<br>
<br>
Usage:<br>
smartant-cli [flags]<br>
<br>
Flags:<br>
-a, --age int       persons age<br>
-h, --help          help for smartant-cli<br>
-n, --name string   persons name<br>
$ ./smartant-cli -a 11 -n "xuel"<br>
name is xuel, age is 11%<br>
</pre><br>
<h3>实现带有子命令的clis</h3>在执行cobra.exe init demo之后，继续使用cobra为demo添加子命令test：<br>
<h4>生成sysinfo子命令</h4><pre class="prettyprint">$ /Users/xuel/workspace/goworkspace/bin/cobra add sysinfo<br>
sysinfo created at /Users/xuel/workspace/goworkspace/src/github.com/kaliarch/smartant-cli<br>
$ tree<br>
.<br>
├── LICENSE<br>
├── cmd<br>
│   ├── root.go<br>
│   └── sysinfo.go<br>
├── go.mod<br>
├── go.sum<br>
├── main.go<br>
├── smartant-cli<br>
└── utils<br>
└── utils.go<br>
</pre><br>
<h4>查看子命令</h4><pre class="prettyprint">$ go build -o smartant-cli <br>
$ ./smartant-cli <br>
<br>
smartant-cli is a CLI for SmartAnt applications.<br>
This application is a tool to migrations linux system.<br>
<br>
Usage:<br>
smartant-cli [flags]<br>
smartant-cli [command]<br>
<br>
Available Commands:<br>
help        Help about any command<br>
sysinfo     A brief description of your command<br>
<br>
Flags:<br>
-a, --age int       persons age<br>
-h, --help          help for smartant-cli<br>
-n, --name string   persons name<br>
<br>
Use "smartant-cli [command] --help" for more information about a command.<br>
$ ./smartant-cli sysinfo -h<br>
A longer description that spans multiple lines and likely contains examples<br>
and usage of using your command. For example:<br>
<br>
Cobra is a CLI library for Go that empowers applications.<br>
This application is a tool to generate the needed files<br>
to quickly create a Cobra application.<br>
<br>
Usage:<br>
smartant-cli sysinfo [flags]<br>
<br>
Flags:<br>
-h, --help   help for sysinfo<br>
</pre><br>
<h4>编写子命令</h4>sysinfo.go：<br>
<pre class="prettyprint">/*<br>
Copyright © 2021 NAME HERE <EMAIL ADDRESS><br>
<br>
Licensed under the Apache License, Version 2.0 (the "License");<br>
you may not use this file except in compliance with the License.<br>
You may obtain a copy of the License at<br>
<br>
http://www.apache.org/licenses/LICENSE-2.0<br>
<br>
Unless required by applicable law or agreed to in writing, software<br>
distributed under the License is distributed on an "AS IS" BASIS,<br>
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.<br>
See the License for the specific language governing permissions and<br>
limitations under the License.<br>
*/<br>
package cmd<br>
<br>
import (<br>
"fmt"<br>
"github.com/kaliarch/smartant-cli/utils"<br>
<br>
"github.com/spf13/cobra"<br>
)<br>
<br>
var (<br>
host, pwd, username string<br>
port                int<br>
command             string<br>
)<br>
<br>
// sysinfoCmd represents the sysinfo command<br>
var sysinfoCmd = &cobra.Command&#123;<br>
Use:   "sysinfo",<br>
Short: "check sys info message",<br>
Long: `A longer description that spans multiple lines and likely contains examples<br>
and usage of using your command. For example:<br>
<br>
Cobra is a CLI library for Go that empowers applications.<br>
This application is a tool to generate the needed files<br>
to quickly create a Cobra application.`,<br>
Run: func(cmd *cobra.Command, args []string) &#123;<br>
    if len(host) == 0 || len(pwd) == 0 &#123;<br>
        cmd.Help()<br>
        return<br>
    &#125;<br>
    fmt.Println("sysinfo called")<br>
    utils.Sysinfo(host, pwd, username, port, command)<br>
    fmt.Println("sysinfo called commpled")<br>
&#125;,<br>
&#125;<br>
<br>
func init() &#123;<br>
rootCmd.AddCommand(sysinfoCmd)<br>
<br>
// Here you will define your flags and configuration settings.<br>
<br>
// Cobra supports Persistent Flags which will work for this command<br>
// and all subcommands, e.g.:<br>
// sysinfoCmd.PersistentFlags().String("foo", "", "A help for foo")<br>
<br>
// Cobra supports local flags which will only run when this command<br>
// is called directly, e.g.:<br>
// sysinfoCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")<br>
sysinfoCmd.Flags().StringVarP(&host, "host", "i", "", "host ip addr")<br>
sysinfoCmd.Flags().StringVarP(&username, "username", "u", "", "host username")<br>
sysinfoCmd.Flags().StringVarP(&command, "command", "c", "", "command")<br>
sysinfoCmd.Flags().StringVarP(&pwd, "pwd", "p", "", "host password")<br>
sysinfoCmd.Flags().IntVarP(&port, "port", "P", 0, "host port")<br>
&#125; <br>
</pre><br>
utils.go：<br>
<pre class="prettyprint">package utils<br>
<br>
import (<br>
"bytes"<br>
"fmt"<br>
"golang.org/x/crypto/ssh"<br>
"net"<br>
"strings"<br>
//"strconv"<br>
"log"<br>
)<br>
<br>
// smartant-cli<br>
func Show(name string, age int) &#123;<br>
fmt.Printf("name is %s, age is %d", name, age)<br>
&#125;<br>
<br>
func sshConnect(user, pwd, host string, port int) (*ssh.Session, error) &#123;<br>
var (<br>
    auth         []ssh.AuthMethod<br>
    addr         string<br>
    clientConfig *ssh.ClientConfig<br>
    client       *ssh.Client<br>
    session      *ssh.Session<br>
    err          error<br>
)<br>
// get auth method<br>
auth = make([]ssh.AuthMethod, 0)<br>
auth = append(auth, ssh.Password(pwd))<br>
<br>
// host key callbk<br>
hostKeyCallbk := func(host string, remote net.Addr, key ssh.PublicKey) error &#123;<br>
    return nil<br>
&#125;<br>
clientConfig = &ssh.ClientConfig&#123;<br>
    User:            user,<br>
    Auth:            auth,<br>
    HostKeyCallback: hostKeyCallbk,<br>
    BannerCallback:  nil,<br>
    //ClientVersion:     "",<br>
    //HostKeyAlgorithms: nil,<br>
    //Timeout: 10000000,<br>
&#125;<br>
<br>
// connet to ssh<br>
addr = fmt.Sprintf("%s:%d", host, port)<br>
<br>
if client, err = ssh.Dial("tcp", addr, clientConfig); err != nil &#123;<br>
    return nil, err<br>
&#125;<br>
<br>
// create session<br>
if session, err = client.NewSession(); err != nil &#123;<br>
    return nil, err<br>
&#125;<br>
return session, nil<br>
&#125;<br>
<br>
func Sysinfo(host, pwd, username string, port int, cmd string) &#123;<br>
var stdOut, stdErr bytes.Buffer<br>
// 使用用户名，密码登陆<br>
session, err := sshConnect(username, pwd, host, port)<br>
if err != nil &#123;<br>
    log.Fatal(err)<br>
&#125;<br>
defer session.Close()<br>
<br>
session.Stdout = &stdOut<br>
session.Stderr = &stdErr<br>
<br>
session.Run(cmd)<br>
fmt.Println(strings.Replace(stdOut.String(), "\n", " ", -1))<br>
&#125; <br>
</pre><br>
执行测试：<br>
<pre class="prettyprint">$ ./smartant-cli sysinfo<br>
A longer description that spans multiple lines and likely contains examples<br>
and usage of using your command. For example:<br>
<br>
Cobra is a CLI library for Go that empowers applications.<br>
This application is a tool to generate the needed files<br>
to quickly create a Cobra application.<br>
<br>
Usage:<br>
smartant-cli sysinfo [flags]<br>
<br>
Flags:<br>
-c, --command string    command<br>
-h, --help              help for sysinfo<br>
-i, --host string       host ip addr<br>
-P, --port int          host port<br>
-p, --pwd string        host password<br>
-u, --username string   host username<br>
<br>
$ ./smartant-cli sysinfo -i 121.3.10.55 -u root -P 22 -p xxxxxxx -c "cat /etc/hosts"<br>
sysinfo called<br>
::1     localhost       localhost.localdomain   localhost6      localhost6.localdomain6  127.0.0.1      localhost       localhost.localdomain   localhost4      localhost4.localdomain4 127.0.0.1   localhost        localhost 127.0.0.1     hw-server       hw-server  <br>
sysinfo called commpled<br>
</pre><br>
<h3>其他</h3>Cobra非常强大，能够帮助我们快速创建命令行工具，但是如果直接仅仅写一个非常简单的命令行工具，flag选项非常少，golang built-in的flag库够了。当然使用看个人选择，Cobra更适合复杂的命令行工具。<br>
<br>参考链接：<br>
<ol><li><a href="https://github.com/spf13/cobra" rel="nofollow" target="_blank">https://github.com/spf13/cobra</a></li><li><a href="https://www.huweihuang.com/golang-notes/framework/cobra/cobra-usage.html" rel="nofollow" target="_blank">https://www.huweihuang.com/gol ... .html</a></li><li><a href="https://juejin.cn/post/6924541628031959047" rel="nofollow" target="_blank">https://juejin.cn/post/6924541628031959047</a></li><li><a href="https://o-my-chenjian.com/2017/09/20/Using-Cobra-With-Golang/" rel="nofollow" target="_blank">https://o-my-chenjian.com/2017 ... lang/</a></li></ol><br>
<br>原文链接：<a href="https://juejin.cn/post/6983299467537547294" rel="nofollow" target="_blank">https://juejin.cn/post/6983299467537547294</a>，作者：薛磊
                                
                                                              
</div>
            