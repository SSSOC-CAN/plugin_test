package shared

import (
	"context"

	proto "github.com/SSSOC-CAN/plugin_test/protos"
	"github.com/dapr/components-contrib/state"
	"github.com/hashicorp/go-plugin"
	"google.golang.org/grpc"
)

var Handshake = plugin.HandshakeConfig{
	// This isn't required when using VersionedPlugins
	ProtocolVersion:  1,
	MagicCookieKey:   "BASIC_PLUGIN",
	MagicCookieValue: "76d3865e-360a-416a-bdf3-7f9891a4a2b8",
}

const (
	ProtocolGRPC = "state_grpc"
)

// PluginMap is the map of plugins we can dispense.
var PluginMap = map[string]plugin.Plugin{
	ProtocolGRPC: &GRPCStatePlugin{},
}

type GRPCStatePlugin struct {
	plugin.Plugin
	Impl state.Store
}

func (p *GRPCStatePlugin) GRPCServer(broker *plugin.GRPCBroker, s *grpc.Server) error {
	proto.RegisterStateServer(s, &GRPCServer{Impl: p.Impl})
	return nil
}

func (p *GRPCStatePlugin) GRPCClient(ctx context.Context, broker *plugin.GRPCBroker, c *grpc.ClientConn) (interface{}, error) {
	return &GRPCClient{client: proto.NewStateClient(c)}, nil
}
