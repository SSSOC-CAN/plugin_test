package main

import (
	"fmt"
	"os"
	"os/exec"

	"github.com/SSSOC-CAN/plugin_test/shared"
	"github.com/dapr/components-contrib/state"
	"github.com/hashicorp/go-plugin"
)

func main() {
	client := plugin.NewClient(&plugin.ClientConfig{
		HandshakeConfig:  shared.Handshake,
		Plugins:          shared.PluginMap,
		SyncStdout:       os.Stdout,
		Cmd:              exec.Command("sh", "-c", "python plugin.py"),
		AllowedProtocols: []plugin.Protocol{plugin.ProtocolGRPC},
	})
	defer client.Kill()
	cl, err := client.Client()
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	raw, err := cl.Dispense(shared.ProtocolGRPC)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	plug := raw.(state.Store)
	err = plug.Init(state.Metadata{})
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	os.Exit(0)
}
